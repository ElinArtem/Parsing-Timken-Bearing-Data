import requests as rq
import json
import math
from bs4 import BeautifulSoup as bs

# Constants
BASE_URL = "https://cad.timken.com"
HEADERS = {
    "User-Agent": "User-Agent",
    "Accept": "Accept",
    "Upgrade-Insecure-Requests": "1",
}


# File Management Plugins
class FileManager:
    @staticmethod
    def connect_json(file_name="all_category.json"):
        print("Connecting to JSON file!")
        with open(file_name, encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def save_to_file(content, file_name: str):
        with open(file_name, "a", encoding="utf-16") as file:
            file.write(str(content).replace("'", '"') + ",\n")

    @staticmethod
    def save_to_file_json(data, file_name: str):
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data, file)
        print("File saved!")


# HTTP Request Plugin
class Requester:
    @staticmethod
    def get_html(url):
        response = rq.get(url, headers=HEADERS)
        return response.content

    @staticmethod
    def get_soup(response):
        if response is None:
            raise TypeError("Received a null pointer reference as input.")
        try:
            return bs(response, "html.parser")
        except Exception as e:
            raise e


# Content Processing Plugins
class ContentParser:
    @staticmethod
    def calculate_pages(soup, page_size):
        cont = str(soup.find("span", id="pageInfo").text)
        total_items = int(cont.split(" ")[-1])
        return math.ceil(total_items / page_size)

    @staticmethod
    def get_table(soup):
        table = soup.find("table", id="plp-table-filter")
        items_box = table.find_all("a", class_="plp-itemlink")
        return [{"name": item.text, "href": item["href"]} for item in items_box]

    @staticmethod
    def get_content_item(soup):
        images = ContentParser.parse_images(soup)
        info = ContentParser.parse_info(soup)
        return {"image": images, "info": info}

    @staticmethod
    def parse_images(soup):
        image_div = soup.find("div", class_="ad-thumbs") or soup.find(
            "div", class_="ad-image"
        )
        if image_div:
            return [
                img.get("href") or img.get("src")
                for img in image_div.find_all(["a", "img"])
            ]
        return ["None"]

    @staticmethod
    def parse_info(soup):
        tables_div = soup.find("div", id="plp-item-page-specs")
        table_groups = tables_div.find_all("div", class_="group")
        all_tables = []

        for table_group in table_groups:
            if header := table_group.find("h3"):
                name = header.text
                table = {name: []}
                for row in table_group.find_all("tr"):
                    row_data = [td.text for td in row.find_all("td")]
                    table[name].append(
                        {
                            "name": row_data[0],
                            "value": row_data[1] if len(row_data) > 1 else None,
                        }
                    )
                all_tables.append(table)
        return all_tables


# Data Collection Plugin
class DataCollector:
    @staticmethod
    def take_items():
        categories = FileManager.connect_json()
        done = FileManager.connect_json("bb_done.json")

        for category in categories:
            if category["name"] not in done:
                print(f'Starting collection for {category["name"]}')
                if "viewitems" in category["href"]:
                    url = BASE_URL + category["href"]
                    soup = Requester.get_soup(Requester.get_html(url))
                    pages = ContentParser.calculate_pages(soup, 100)

                    category_items = [
                        ContentParser.get_table(
                            Requester.get_soup(
                                Requester.get_html(
                                    f"{url}?pagesize=100&pagenum={i+1}&selecteduom=1"
                                )
                            )
                        )
                        for i in range(pages)
                    ]

                    DataCollector.process_pages(category, category_items)

    @staticmethod
    def process_pages(category, category_items):
        for page_num, page in enumerate(category_items, 1):
            print(f"Processing page {page_num} for category {category['name']}")
            for item in page:
                DataCollector.process_item(item, category)

    @staticmethod
    def process_item(item, category):
        if item["name"] not in FileManager.connect_json("bb_done.json"):
            print(f'Processing item {item["name"]}')
            try:
                info = {
                    "name": item["name"],
                    "category": category["name"],
                    **ContentParser.get_content_item(
                        Requester.get_soup(Requester.get_html(BASE_URL + item["href"]))
                    ),
                }
                FileManager.save_to_file(info, f'{category["name"][0]}.txt')
            except rq.exceptions.ConnectionError:
                FileManager.save_to_file(item, "skipted.txt")

    @staticmethod
    def process_skipped_items():
        skipped_items = FileManager.connect_json("skip.json")
        for item in skipped_items:
            print(f'Processing skipped item {item["name"]}')
            try:
                info = {
                    "name": item["name"],
                    "category": [
                        "Tapered Roller Bearings",
                        "TS (Tapered Single)",
                        "TS Imperial",
                    ],
                    **ContentParser.get_content_item(
                        Requester.get_soup(Requester.get_html(BASE_URL + item["href"]))
                    ),
                }
                FileManager.save_to_file(info, "Tapered Roller Bearings.txt")
            except rq.exceptions.ConnectionError:
                FileManager.save_to_file(item, "skipted.txt")


# Main Execution
def main():
    DataCollector.take_items()


if __name__ == "__main__":
    main()
