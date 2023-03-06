import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'WAD_2023_7C.settings')
import django

django.setup()
from yumyay.models import Cuisine, Recipe
from populate_data import *
def populate():

    def add_cuisine(name):
        cuis = Cuisine.objects.get_or_create(name=name)[0]
        cuis.name = name
        cuis.save()
        return name

    def add_recipe(name, description, category, cuis, ingredients, instructions, author, image):
        recp = Recipe.objects.get_or_create(name=name, description=description, category=category, cuisine=cuis,
                                            ingredients=ingredients, instructions=instructions, author=author,
                                            image=image)[0]
        recp.name = name
        recp.description = description
        recp.category = category
        recp.cuisine = cuis
        recp.ingredients = ingredients
        recp.instructions = instructions
        recp.author = author
        recp.image = image
        recp.save()
        return recp

    for cuisine, cuisine_data in cuisines.items():
        c = add_cuisine(cuisine_data['name'])
        for r in cuisine_data['recipes']:
            add_recipe(r['name'], r['description'], r['category'], r['cuisine'], r['ingredients'], r['instructions'],
                       r['author'], "recipe_images/cat.jpg")


if __name__ == '__main__':
    print('starting populate script')
    populate()
    print('populate script complete')
