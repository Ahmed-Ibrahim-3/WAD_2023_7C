from django import forms
from django.contrib.auth.models import User
from yumyay.models import Recipe


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)


class RecipeForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Name of recipe: ")
    description = forms.CharField(max_length=1024, help_text="Description of recipe: ")
    ingredients = forms.CharField(max_length=1024, help_text="Ingredients: ",
                                  widget=forms.Textarea(attrs={'rows': 8, 'cols': 100}))
    instructions = forms.CharField(max_length=1024, help_text="Instructions: ",
                                   widget=forms.Textarea(attrs={'rows': 12, 'cols': 100}))
    category = forms.ChoiceField(help_text='Category', choices=(
        ('C', 'Cooking'),
        ('B', 'Baking'),
    ))
    image = forms.ImageField(required=False)

    class Meta:
        model = Recipe
        exclude = ('likes','author')

