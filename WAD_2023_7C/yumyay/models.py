from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = "categories"
    
class Cuisine(models.Model):
    name = models.CharField(max_length=128, unique=True)

class Ingredient(models.Model):
    name = models.CharField(max_length=128, unique=True)

class Recipe(models.Model):
    name = models.CharField(max_length=128, unique=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    default=models.DateTimeField()

class RecipeHasIngredient(models.Model):
    measure = models.CharField(max_length=128)
    quantity = models.FloatField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    # change on_delete?
    # if remove one ingredient, all recipes with it are also removed
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

class Instruction(models.Model):
    index = models.IntegerField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    content = models.BooleanField()
