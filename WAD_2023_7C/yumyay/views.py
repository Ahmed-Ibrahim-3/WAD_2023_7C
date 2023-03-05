from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from yumyay.models import Recipe, UserProfile, UserLikesRecipe
from django.contrib.auth.decorators import login_required


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
# still to be fixed
def recipe_cooking(request):
    context_dict = {}
    try:
        recipe = Recipe.objects.get(name = "content")
    except Recipe.DoesNotExist:
        recipe = None

    context_dict['recipe'] = recipe
    return render(request, 'yumyay/recipe.html', context_dict)


def recipe_baking(request):
    return render(request, 'yumyay/recipe.html')

class LikeRecipeView(View):
    def get(self, request):
        recipe_name = request.GET['name']
        username = request.GET['user']

        try:
            recipe = Recipe.objects.get(name=recipe_name)
        except Recipe.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)
        
        try:
            user = UserProfile.objects.get(username=username)
        except UserProfile.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)
    
        recipe.likes = recipe.likes + 1
        recipe.save()

        user_likes_recipe = UserLikesRecipe.objects.get_or_create(user=user, recipe=recipe)
        user_likes_recipe.likes = True
        user_likes_recipe.save()

        return HttpResponse(recipe.likes)
    
class UnlikeRecipeView(View):
    def get(self, request):
        recipe_name = request.GET['name']
        username = request.GET['user']

        try:
            recipe = Recipe.objects.get(name=recipe_name)
        except Recipe.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)
        
        try:
            user = UserProfile.objects.get(username=username)
        except UserProfile.DoesNotExist:
            return HttpResponse(0)
        except ValueError:
            return HttpResponse(0)
    
        recipe.likes = recipe.likes - 1
        recipe.save()

        user_likes_recipe = UserLikesRecipe.objects.get_or_create(user=user, recipe=recipe)
        user_likes_recipe.likes = False
        user_likes_recipe.save()

        return HttpResponse(recipe.likes)
    
# TODO: error handling if request is invalid?
class HasUserLikedRecipe(View):
    def get(self, request):
        recipe_name = request.GET['name']
        username = request.GET['user']

        try:
            recipe = Recipe.objects.get(name=recipe_name)
        except Recipe.DoesNotExist:
            return HttpResponse(0)
        except ValueError:
            return HttpResponse(0)
        
        try:
            user = UserProfile.objects.get(username=username)
        except UserProfile.DoesNotExist:
            return HttpResponse(0)
        except ValueError:
            return HttpResponse(0)

        user_likes_recipe = UserLikesRecipe.objects.get_or_create(user=user, recipe=recipe)
        user_likes_recipe.save()

        if(user_likes_recipe.liked):
            return HttpResponse(1)
        else:
            return HttpResponse(0)