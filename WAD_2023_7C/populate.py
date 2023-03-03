import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'WAD_2023_7C.settings')
import django

django.setup()
from yumyay.models import Cuisine, Recipe


def populate():
    indian = [
        {
            'name': 'content',
            'description': 'content',
            'category': 'cooking',
            'cuisine': 'indian',
            'ingredients': 'content',
            'instructions': 'content'

        }
    ]
    thai = [
        {
            'name': 'content2',
            'description': 'content',
            'category': 'cooking',
            'cuisine': 'thai',
            'ingredients': 'content',
            'instructions': 'content'

        }
    ]
    chinese = [
        {
            'name': 'content3',
            'description': 'content',
            'category': 'cooking',
            'cuisine': 'chinese',
            'ingredients': 'content',
            'instructions': 'content'

        }
    ]
    italian = [
        {
            'name': 'content4',
            'description': 'content',
            'category': 'cooking',
            'cuisine': 'italian',
            'ingredients': 'content',
            'instructions': 'content'

        }
    ]
    mexican = [
        {
            'name': 'content5',
            'description': 'content',
            'category': 'cooking',
            'cuisine': 'mexican',
            'ingredients': 'content',
            'instructions': 'content'

        }
    ]
    greek = [
        {
            'name': 'content6',
            'description': 'content',
            'category': 'cooking',
            'cuisine': 'greek',
            'ingredients': 'content',
            'instructions': 'content'

        }
    ]
    cake = [
        {
            'name': 'content7',
            'description': 'content',
            'category': 'baking',
            'cuisine': 'cake',
            'ingredients': 'content',
            'instructions': 'content'

        }
    ]
    brownie = [
        {
            'name': 'content8',
            'description': 'content',
            'category': 'baking',
            'cuisine': 'brownie',
            'ingredients': 'content',
            'instructions': 'content'

        }
    ]
    bread = [
        {
            'name': 'content9',
            'description': 'content',
            'category': 'baking',
            'cuisine': 'bread',
            'ingredients': 'content',
            'instructions': 'content'

        }
    ]
    pastries = [
        {
            'name': 'content10',
            'description': 'content',
            'category': 'baking',
            'cuisine': 'pastries',
            'ingredients': 'content',
            'instructions': 'content'

        }
    ]
    cupcakes = [
        {
            'name': 'content11',
            'description': 'content',
            'category': 'baking',
            'cuisine': 'cupcakes',
            'ingredients': 'content',
            'instructions': 'content'

        }
    ]
    cookies = [
        {
            'name': 'content12',
            'description': 'content',
            'category': 'baking',
            'cuisine': 'cookies',
            'ingredients': 'content',
            'instructions': 'content'

        }
    ]

    cuisines = {
        'Indian': {'name': 'indian', 'recipes': indian},
        'Thai': {'name': 'Thai', 'recipes': thai},
        'Chinese': {'name': 'Chinese', 'recipes': chinese},
        'Italian': {'name': 'Italian', 'recipes': italian},
        'Mexican': {'name': 'Mexican', 'recipes': mexican},
        'Greek': {'name': 'Greek', 'recipes': greek},
        'Cake': {'name': 'Cake', 'recipes': cake},
        'Brownies': {'name': 'Brownies', 'recipes': brownie},
        'Bread': {'name': 'Bread', 'recipes': bread},
        'Pastries': {'name': 'Pastries', 'recipes': pastries},
        'Cupcakes': {'name': 'Cupcakes', 'recipes': cupcakes},
        'Cookies': {'name': 'Cookies', 'recipes': cookies}
    }

    def add_cuisine(name):
        print("weeeeeeee")
        cuis = Cuisine.objects.get_or_create(name=name)[0]
        cuis.save()
        return name

    def add_recipe(name, description, cuis, ingredients, instructions):
        recp = Recipe.objects.get_or_create(name=name, description=description,
                                            cuisine=cuis, ingredients=ingredients, instructions=instructions)[0]
        print("wooooooo")
        recp.name = name
        print(name)
        recp.description = description
        recp.cuisine = cuis
        recp.ingredients = ingredients
        recp.instructions = instructions
        recp.save()
        return recp

    for cuisine, cuisine_data in cuisines.items():
        c = add_cuisine(cuisine_data['name'])
        for r in cuisine_data['recipes']:
            add_recipe(r['name'], r['description'], c, r['ingredients'], r['instructions'])

    for c in Cuisine.objects.all():
        for r in Recipe.objects.filter(cuisine=c):
            print(f'- {c}:{r}')


if __name__ == '__main__':
    print('starting populate script')
    populate()
