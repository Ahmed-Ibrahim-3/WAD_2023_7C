from pyexpat.errors import messages

from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse
from yumyay.forms import UserForm, EditDetailsForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from yumyay.models import Recipe, UserProfile, UserLikesRecipe, User, Cuisine, Recipe
from yumyay.forms import RecipeForm
from django.templatetags.static import static


# Create your views here.
def home(request):
    context_dict = {}

    amount = 5
    recipe_list = Recipe.objects.order_by('-likes')[:amount]
    context_dict['recipes'] = recipe_list
    context_dict['page'] = 'home'
    return render(request, 'yumyay/home.html', context_dict)


def log_in(request):
    return render(request, 'yumyay/login.html')


def account(request):
    recipes = Recipe.objects.filter(author=request.user.username)
    context_dict = {"recipes": recipes}
    return render(request, 'yumyay/account.html', context_dict)


def cooking(request):
    context_dict = {}
    recipes = Recipe.objects.filter(category='C').order_by('-likes')
    if len(recipes) > 0:
        context_dict = {'top_recipe': recipes[0], 'all_recipes': recipes}
    context_dict['page'] = 'cooking'
    return render(request, 'yumyay/cooking.html', context=context_dict)


def baking(request):
    context_dict = {}
    recipes = Recipe.objects.filter(category='B').order_by('-likes')
    if len(recipes) > 0:
        context_dict = {'top_recipe': recipes[0], 'all_recipes': recipes}
    context_dict['page'] = 'baking'
    return render(request, 'yumyay/baking.html', context=context_dict)


@login_required
def add_recipe(request):
    form = RecipeForm()

    if request.method == 'POST':
        form = RecipeForm(request.POST)

        if form.is_valid():
            recipe = form.save(commit=True)
            username = None
            if request.user.is_authenticated:
                username = request.user.username
            recipe.author = username
            # recipe.image = form.image
            if 'image' in request.FILES:
                recipe.image = request.FILES['image']
                print(request.FILES['image'])
            else:
                recipe.image = 'recipe_images/missing_image.png'
            recipe.save()
            return redirect('/')
        else:
            print(form.errors)

    return render(request, 'yumyay/add_recipe.html', {'form': form, 'page':'add_recipe'})


def register(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            registered_user = authenticate(username=user_form.cleaned_data['username'],
                                    password=user_form.cleaned_data['password'],
            )
            login(request, registered_user)
            return redirect('/')
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'yumyay/register.html', context={'user_form': user_form})

@login_required
def edit_details(request):
    if request.method == 'POST':
        form = EditDetailsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('yumyay:account')
    else:
        form = EditDetailsForm(instance=request.user)
    return render(request, 'yumyay/edit_details.html', {'form': form})

def delete_recipe(request, id):
    recipe = Recipe.objects.filter(id=id)
    recipe.delete()
    return redirect(reverse('yumyay:account'))

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('yumyay:home'))
            else:
                return HttpResponse("Your yumyay account is disabled")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'yumyay/login.html')


def user_logout(request):
    logout(request)
    return redirect(reverse('yumyay:home'))


def recipe(request, cuisine_name_slug, recipe_id):
    context_dict = {}
    try:
        recipe = Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        recipe = None
    context_dict['cuisine'] = cuisine_name_slug
    context_dict['recipe'] = recipe
    return render(request, 'yumyay/recipe.html', context=context_dict)


def cuisine(request, cuisine_name_slug):
    context_dict = {}
    recipe_list = Recipe.objects.filter(cuisine=str.upper(cuisine_name_slug))
    top_recipe = recipe_list.order_by('likes')
    if len(top_recipe) > 0:
        context_dict['top_recipe'] = top_recipe[0]
    else:
        context_dict['top_recipe'] = None
    context_dict['cuisine'] = cuisine_name_slug
    context_dict['recipes'] = recipe_list
    return render(request, 'yumyay/cuisine.html', context=context_dict)


class LikeRecipeView(View):
    def post(self, request):
        if request.method == 'POST':
            username = request.POST['username']
            recipe_id = request.POST['recipe']
            like = request.POST['liked']
            
            if like == 'like':
                like = True
            else:
                like = False

            try:
                recipe = Recipe.objects.get(id=recipe_id)
            except Recipe.DoesNotExist:
                return HttpResponse(-1)
            except ValueError:
                return HttpResponse(-1)

            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return HttpResponse(-1)
            except ValueError:
                return HttpResponse(-1)

            try:
                user_likes_recipe = UserLikesRecipe.objects.get_or_create(user=user, recipe=recipe)[0]
                if user_likes_recipe.liked == like:
                    return HttpResponse(recipe.likes)
            except ValueError:
                return HttpResponse(-1)

            if like:
                recipe.likes = recipe.likes + 1
                user_likes_recipe.liked = True
            else:
                recipe.likes = recipe.likes - 1
                user_likes_recipe.liked = False
            recipe.save()
            user_likes_recipe.save()

            return HttpResponse(recipe.likes)


class HasUserLikedRecipe(View):
    def get(self, request):
        recipe_id = request.GET['recipeId']
        username = request.GET['user']
        try:
            recipe = Recipe.objects.get(id=recipe_id)
        except Recipe.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)

        try:
            user = User.objects.get(username=username)
        except UserProfile.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)

        try:
            user_likes_recipe = UserLikesRecipe.objects.get_or_create(user=user, recipe=recipe)[0]
        except ValueError:
            return HttpResponse(-1)

        if (user_likes_recipe.liked):
            return HttpResponse(1)
        else:
            return HttpResponse(0)

def delete(request):
      member = User.objects.get(id = request.user.id)
      Recipe.objects.filter(author = member.username).delete()
      member.delete()
      return redirect(reverse('yumyay:home'))