# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class RecipeItem(scrapy.Item):
    # Define the fields for your item here

    recipe_id = scrapy.Field()
    full_name = scrapy.Field()
    title = scrapy.Field()
    image_url = scrapy.Field()
    description = scrapy.Field()
    prep_time = scrapy.Field()            # in minutes
    cook_time = scrapy.Field()            # in minutes
    course = scrapy.Field()               # e.g., main course, salad, etc.
    cuisine = scrapy.Field()              # e.g., Italian, American, etc.
    serving = scrapy.Field()              # serving size
    ingredients = scrapy.Field()          # list of ingredients
    ingredient_count = scrapy.Field()     # num of ingredients
    instructions = scrapy.Field()         # preparation instructions
    notes = scrapy.Field()                # additional notes
    calories = scrapy.Field()             # in kcal
    carbohydrates = scrapy.Field()        # in grams
    protein = scrapy.Field()              # in grams
    fat = scrapy.Field()                  # in grams
    saturated_fat = scrapy.Field()        # in grams
    polyunsaturated_fat = scrapy.Field()  # in grams
    monounsaturated_fat = scrapy.Field()  # in grams
    cholesterol = scrapy.Field()          # in milligrams
    sodium = scrapy.Field()               # in milligrams
    potassium = scrapy.Field()            # in milligrams
    sugar = scrapy.Field()                # in grams
    fiber = scrapy.Field()                # in grams

