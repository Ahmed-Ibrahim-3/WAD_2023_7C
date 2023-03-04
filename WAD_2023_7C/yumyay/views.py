from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse
from yumyay.forms import UserForm
from django.contrib.auth import authenticate, login
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

def register(request):
    registered = False
    
    if request.method == "POST":
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    
    return render(request, 'yumyay/register.html', context = {'user_form': user_form, 'registered': registered})

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


# Nyx fix recipes stuff it's a mess xoxo
def recipe_cooking(request):
    return render(request, 'yumyay/recipe.html')


def recipe_baking(request):
    return render(request, 'yumyay/recipe.html')
