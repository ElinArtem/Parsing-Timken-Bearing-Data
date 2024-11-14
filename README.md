# Timken CAD Scraper

This project is a web scraping tool designed to collect product data from the Timken CAD catalog website. It extracts information on various bearing products, including names, images, and specifications, and saves the collected data in JSON format for further analysis or use.

## Table of Contents
- [Timken CAD Scraper](#timken-cad-scraper)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Setup](#setup)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
  - [Project Structure](#project-structure)
  - [Dependencies](#dependencies)
  - [Contributing](#contributing)

## Features
- **Web Scraping**: Retrieves product details including images and specifications.
- **Data Parsing**: Extracts structured data from HTML into JSON format.
- **Pagination Handling**: Handles multi-page scraping for large datasets.
- **Error Handling**: Captures and logs errors for items that could not be scraped.

## Setup

### Prerequisites
- Python 3.7 or higher
- Basic understanding of web scraping and Python programming.

### Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/timken-cad-scraper.git
    cd timken-cad-scraper
    ```

2. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure file paths (optional):**
   - Modify file names in `FileManager.connect_json()` and `FileManager.save_to_file()` if you want custom paths for input and output files.

## Usage
1. **Run the main script**:
    ```bash
    python scraper.py
    ```
   This will initiate the scraping process, starting with categories defined in `all_category.json`.

2. **Output**:
   - Scraped data will be saved in `.txt` files or JSON files, as specified in the script.
   - Skipped items will be logged in `skipted.txt`.

## Project Structure
- `scraper.py`: Main file containing the web scraping logic and data processing.
- `FileManager`: Handles file operations, including loading JSON files and saving data.
- `Requester`: Manages HTTP requests to the Timken CAD website.
- `ContentParser`: Parses the HTML content to extract required data.
- `DataCollector`: Coordinates the scraping workflow, including pagination and retrying skipped items.

## Dependencies
- `requests`: For making HTTP requests to retrieve HTML content.
- `beautifulsoup4`: For parsing HTML content.
- `json`: For handling JSON data input and output.

Install these dependencies with:
```bash
pip install requests beautifulsoup4
```

## Contributing

Contributions are welcome! Please follow these steps:

 1. Fork the repository.
 2. Create a new branch (git checkout -b feature-name).
 3. Commit your changes (git commit -m "Add feature").
 4. Push to the branch (git push origin feature-name).
 5. Open a pull request.
