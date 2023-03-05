from django import forms
from django.contrib.auth.models import User
from yumyay.models import Recipe


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)


class RecipeForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="name of recipe:")
    description = forms.CharField(max_length=1024, help_text="description of recipe:")
    ingredients = forms.CharField(max_length=1024, help_text="ingredients:")
    instructions = forms.CharField(max_length=1024, help_text="instructions:")
    category = forms.ChoiceField(choices=("Cooking", "Baking"))
    cuisine = forms.ChoiceField(choices=("Indian", "Thai", "Chinese", "Italian", "Mexican", "Greek",
                                         "Cakes", "Brownies", "Bread", "Pastries", "Cupcakes", "Cookies"))
    author = forms.CharField(max_length=64, help_text="Author name")
    image = forms.ImageField()
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Recipe
        exclude = ('likes','author')
