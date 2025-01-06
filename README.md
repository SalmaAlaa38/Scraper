# Scrapy Recipe Scraper

## Overview

This project is a web scraper built using the Scrapy framework to collect recipe data from a food website. It extracts essential details such as recipe titles, ingredients, cooking instructions, nutritional information, and more. This tool is ideal for aggregating recipes or analyzing culinary trends.

## Features

- Scrapes detailed recipe information including:
  - Recipe title and description
  - Ingredients with amounts, units, and notes
  - Preparation and cooking time
  - Nutritional information (calories, protein, fat, carbohydrates, etc.)
  - Instructions and notes
- Handles pagination for seamless scraping of multiple pages.
- Provides a clear and structured output in JSON format.
- Allows configuration for specific pages or entire categories.

## Setup Instructions

### Prerequisites

1. Install Python 3.8 or higher.
2. Install `pip`, the Python package manager.
3. Ensure `virtualenv` is installed for creating isolated environments:
   ```bash
   pip install virtualenv
   ```

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Create and activate a virtual environment:
   ```bash
   virtualenv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Spider

To start the spider, execute the following command:

```bash
scrapy crawl recipes
```

### Customizing Start URLs

You can specify a different starting page by modifying the `start_urls` variable in `RecipeSpider`.

### Output Format

By default, the scraped data is stored in a JSON file named `output.json`. To specify a different output format or file name, use the `-o` flag:

```bash
scrapy crawl recipes -o recipes.json
```

### Example Output

```json
{
  "recipe_id": "49792",
  "full_name": "Cottage Cheese Egg Salad",
  "title": "Egg Salad",
  "image_url": "https://example.com/image.jpg",
  "description": "A delicious egg salad recipe.",
  "prep_time": "10",
  "cook_time": "5",
  "ingredients": [
    {
      "name": "Eggs",
      "amount": "2",
      "unit": "pieces",
      "notes": "Boiled"
    },
    {
      "name": "Mayonnaise",
      "amount": "1",
      "unit": "tbsp",
      "notes": "Low fat"
    }
  ],
  "instructions": [
    "Boil the eggs.",
    "Mix with mayonnaise."
  ],
  "calories": "150",
  "protein": "12g",
  "fat": "10g",
  "carbohydrates": "2g",
  "etc......."
}
```

## Project Structure

```
project_directory/
├── scrapy_project/
│   ├── spiders/
│   │   └── recipe_spider.py  # The main spider
│   ├── items.py             # Defines the structure of scraped items
│   ├── pipelines.py         # Processes scraped data
│   ├── settings.py          # Configures Scrapy settings
├── requirements.txt         # Dependencies
├── README.md                # Project documentation
```

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

Special thanks to the Scrapy community for creating such a robust framework and to the website owners for providing the data used in this project.
