from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'yumyay/home.html')


def log_in(request):
    return render(request, 'yumyay/log_in.html')


def account(request):
    return render(request, 'yumyay/account.html')


def cooking(request):
    return render(request, 'yumyay/cooking.html')


def baking(request):
    return render(request, 'yumyay/baking.html')


def add_recipe(request):
    return render(request, 'yumyay/add_recipe.html')


# Nyx fix recipes stuff it's a mess xoxo
def recipe_cooking(request):
    return render(request, 'yumyay/recipe.html')


def recipe_baking(request):
    return render(request, 'yumyay/recipe.html')
