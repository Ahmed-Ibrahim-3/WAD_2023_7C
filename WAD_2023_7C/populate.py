import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')
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
            'name': 'content',
            'description': 'content',
            'category': 'cooking',
            'cuisine': 'thai',
            'ingredients': 'content',
            'instructions': 'content'

        }
    ]
    chinese = [
        {
            'name': 'content',
            'description': 'content',
            'category': 'cooking',
            'cuisine': 'chinese',
            'ingredients': 'content',
            'instructions': 'content'

        }
    ]
    italian = [
        {
            'name': 'content',
            'description': 'content',
            'category': 'cooking',
            'cuisine': 'italian',
            'ingredients': 'content',
            'instructions': 'content'

        }
    ]
    mexican = [
        {
            'name': 'content',
            'description': 'content',
            'category': 'cooking',
            'cuisine': 'mexican',
            'ingredients': 'content',
            'instructions': 'content'

        }
    ]
    greek = [
        {
            'name': 'content',
            'description': 'content',
            'category': 'cooking',
            'cuisine': 'greek',
            'ingredients': 'content',
            'instructions': 'content'

        }
    ]
    cake = [
        {
            'name': 'content',
            'description': 'content',
            'category': 'baking',
            'cuisine': 'cake',
            'ingredients': 'content',
            'instructions': 'content'

        }
    ]
    brownie = [
        {
            'name': 'content',
            'description': 'content',
            'category': 'baking',
            'cuisine': 'brownie',
            'ingredients': 'content',
            'instructions': 'content'

        }
    ]
    bread = [
        {
            'name': 'bread',
            'description': 'content',
            'category': 'baking',
            'cuisine': 'bread',
            'ingredients': 'content',
            'instructions': 'content'

        }
    ]
    pastries = [
        {
            'name': 'content',
            'description': 'content',
            'category': 'baking',
            'cuisine': 'pastries',
            'ingredients': 'content',
            'instructions': 'content'

        }
    ]
    cupcakes = [
        {
            'name': 'content',
            'description': 'content',
            'category': 'baking',
            'cuisine': 'cupcakes',
            'ingredients': 'content',
            'instructions': 'content'

        }
    ]
    cookies = [
        {
            'name': 'content',
            'description': 'content',
            'category': 'baking',
            'cuisine': 'cookies',
            'ingredients': 'content',
            'instructions': 'content'

        }
    ]

    cuisines = {
        'Indian': indian,
        'Thai': thai,
        'Chinese': chinese,
        'Italian': italian,
        'Mexican': mexican,
        'Greek': greek,
        'Cake': cake,
        'Brownies': brownie,
        'Bread': bread,
        'Pastries': pastries,
        'Cupcakes': cupcakes,
        'Cookies': cookies}

    # write brains of the code
