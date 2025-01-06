import scrapy
from ..items import RecipeItem

class RecipeSpider(scrapy.Spider):
    name = 'recipes'
    start_urls = [
        'https://ohsnapmacros.com/category/pumpkin-recipes/'
    ]
    def parse(self, response):
        recipes_links = response.css('#archive-container a::attr(href)').getall()

        for link in recipes_links:
            yield scrapy.Request(url=link, callback=self.parse_recipe)

        next_page = response.css('.pagination .next::attr(href)').get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)


    def parse_recipe(self, response):
        items = RecipeItem()
        div_recipe = response.css('.wprm-recipe-container')

        # Individual pieces of information
        recipe_id = response.css('a.wprm-recipe-jump::attr(data-recipe)').get()
        full_name = response.css('#main .entry-title::text').get()
        title = div_recipe.css('.wprm-recipe-name.wprm-block-text-bold::text').get()
        image_url = div_recipe.css('img.attachment-250x250::attr(data-src)').get()
        description = div_recipe.css('.wprm-recipe-summary.wprm-block-text-normal span::text').extract()
        prep_time = div_recipe.css('.wprm-recipe-prep_time-minutes::text').get() #mins
        cook_time = div_recipe.css('.wprm-recipe-cook_time-minutes::text').get() #mins
        course = div_recipe.css('.wprm-recipe-course::text').extract() #could be main break salad
        cuisine =  div_recipe.css('.wprm-recipe-cuisine::text').extract()
        serving = div_recipe.css('.wprm-recipe-servings-adjustable-tooltip::text').get()
        instructions = div_recipe.css('.wprm-recipe-instruction-text span::text').extract()
        notes = div_recipe.css('.wprm-recipe-notes li::text').extract()

        # Nutritional information
        calories = div_recipe.css('.wprm-nutrition-label-text-nutrition-container-calories .wprm-nutrition-label-text-nutrition-value::text').get() #kcal
        carbohydrates = div_recipe.css('.wprm-nutrition-label-text-nutrition-container-carbohydrates .wprm-nutrition-label-text-nutrition-value::text').get() #g
        protein = div_recipe.css('.wprm-nutrition-label-text-nutrition-container-protein .wprm-nutrition-label-text-nutrition-value::text').get() #g
        fat = div_recipe.css('.wprm-nutrition-label-text-nutrition-container-fat .wprm-nutrition-label-text-nutrition-value::text').get() #g
        saturated_fat = div_recipe.css('.wprm-nutrition-label-text-nutrition-container-saturated_fat .wprm-nutrition-label-text-nutrition-value::text').get() #g
        polyunsaturated_fat = div_recipe.css('.wprm-nutrition-label-text-nutrition-container-polyunsaturated_fat .wprm-nutrition-label-text-nutrition-value::text').get() #g
        monounsaturated_fat = div_recipe.css('.wprm-nutrition-label-text-nutrition-container-monounsaturated_fat .wprm-nutrition-label-text-nutrition-value::text').get() #g
        cholesterol = div_recipe.css('.wprm-nutrition-label-text-nutrition-container-cholesterol .wprm-nutrition-label-text-nutrition-value::text').get() #mg
        sodium = div_recipe.css('.wprm-nutrition-label-text-nutrition-container-sodium .wprm-nutrition-label-text-nutrition-value::text').get() #mg
        potassium = div_recipe.css('.wprm-nutrition-label-text-nutrition-container-potassium .wprm-nutrition-label-text-nutrition-value::text').get() #mg
        sugar = div_recipe.css('.wprm-nutrition-label-text-nutrition-container-sugar .wprm-nutrition-label-text-nutrition-value::text').get() #g
        fiber = div_recipe.css('.wprm-nutrition-label-text-nutrition-container-fiber .wprm-nutrition-label-text-nutrition-value::text').get() #g

        # Scraping ingredients
        ingredients = []
        ingredients_groups = div_recipe.css('.wprm-recipe-ingredient')
        for ingredient in ingredients_groups:
            amount = ingredient.css('.wprm-recipe-ingredient-amount::text').get()
            unit = ingredient.css('.wprm-recipe-ingredient-unit::text').get()
            name = ingredient.css('.wprm-recipe-ingredient-name::text').get()
            notes = ingredient.css('.wprm-recipe-ingredient-notes-faded::text').get()

            # Combine the details into a dictionary for better structure
            ingredients.append({
                'amount': amount,
                'unit': unit,
                'name': name,
                'notes': notes,
            })

        ingredient_count = len(ingredients)

        # Storing all the extracted data in items
        items['recipe_id'] = recipe_id
        items['full_name'] = full_name
        items['title'] = title
        items['image_url'] = image_url
        items['description'] = description
        items['prep_time'] = prep_time
        items['cook_time'] = cook_time
        items['course'] = course
        items['cuisine'] = cuisine
        items['serving'] = serving
        items['ingredients'] = ingredients
        items['ingredient_count'] = ingredient_count
        items['instructions'] = instructions
        items['notes'] = notes
        items['calories'] = calories
        items['carbohydrates'] = carbohydrates
        items['protein'] = protein
        items['fat'] = fat
        items['saturated_fat'] = saturated_fat
        items['polyunsaturated_fat'] = polyunsaturated_fat
        items['monounsaturated_fat'] = monounsaturated_fat
        items['cholesterol'] = cholesterol
        items['sodium'] = sodium
        items['potassium'] = potassium
        items['sugar'] = sugar
        items['fiber'] = fiber

        yield items