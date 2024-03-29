import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.


class Cuisine(models.Model):
    name = models.CharField(max_length=64, unique=True)
    img = models.ImageField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Cuisine, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    CATEGORIES = (
        ("C", "Cooking"),
        ("B", "Baking")
    )
    CUISINES = [
        ('Cooking', (
            ('CHINESE', 'Chinese'),
            ('INDIAN', 'Indian'),
            ('ITALIAN', 'Italian'),
            ('GREEK', 'Greek'),
            ('MEXICAN', 'Mexican'),
            ('THAI', 'Thai'),
        )
         ),
        ('Baking', (
            ('BREAD', 'Bread'),
            ('BROWNIES', 'Brownies'),
            ('CAKE', 'Cake'),
            ('COOKIES', 'Cookies'),
            ('CUPCAKES', 'Cupcakes'),
            ('PASTRIES', 'Pastries'),
        )
         ),
    ]
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    category = models.CharField(max_length=128, choices=CATEGORIES)
    cuisine = models.CharField(max_length=128, choices=CUISINES)
    ingredients = models.CharField(max_length=4096)
    instructions = models.CharField(max_length=4096)
    author = models.CharField(max_length=64, default="")
    image = models.ImageField(upload_to='recipe_images/')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forename = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    emailAddress = models.EmailField(max_length=128)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.user.username


class UserLikesRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)
