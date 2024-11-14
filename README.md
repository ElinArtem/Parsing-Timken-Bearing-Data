# Timken CAD Scraper

This project is a web scraping tool designed to collect product data from the Timken CAD catalog website. It extracts information on various bearing products, including names, images, and specifications, and saves the collected data in JSON format for further analysis or use.

## Table of Contents
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)

## Features
- **Web Scraping**: Retrieves product details including images and specifications.
-aper

This project Extracts structured data from HTML into JSON format.
-en CAD Scraper

This proj Handles multi-page scraping for large datasets.
- Timken CAD Scraper
 Captures and logs errors for items that could not be scraped.

## Setup

### Prerequisites
- Python 3.7 or higher
- Basic understanding of web scraping and Python programming.

### Installation
1.ion on various bearing prod   e’s a structured README.md for your project:

# Timken CAD Scraper

This project is a web scraping tool designed
2. Install the required packages:
   e’s a structured README.md for your project:

# Timke
3. Configure file paths (optional):
   - Modify file names inE.md for your project:

# Timkand FileManager.save_to_file() if you want custom paths for input and output files.

## Usage
1.aper

This project is a w
   python scraper.py
       This will initiate the scraping process, starting with categories defined inject is a web scrapin

2. Output:
   - Scraped data will be saved in .txt files or JSON files, as specified in the script.
   - Skipped items will be logged ins a web scrapin

## Project Structure
- scraper.py: Main file containing the web scraping logic and data processing.
-er

This projec Handles file operations, including loading JSON files and saving data.
-is project is Manages HTTP requests to the Timken CAD website.
-Timken CAD Scrape Parses the HTML content to extract required data.
-imken CAD Scraper Coordinates the scraping workflow, including pagination and retrying skipped items.

## Dependencies
-ool designed For making HTTP requests to retrieve HTML content.
-mken CAD Scraper

 For parsing HTML content.
- json: For handling JSON data input and output.

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
