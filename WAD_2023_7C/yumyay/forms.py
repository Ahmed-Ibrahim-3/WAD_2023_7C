from django import forms
from yumyay.models import Category, Cuisine, Recipe
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)

class RecipeForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text='Name: ', required=True)
    # use class method to set author on form submit?
    author = None
    category = forms.ChoiceField(queryset=Category.objects.all(), required=True, help_text='Category: ')
    cuisine = forms.ChoiceField(queryset=Cuisine.objects.all(), required=True, help_text='Cuisine: ')
    # ingredients, instructions
    image = forms.ImageField(help_text='An image related to the recipe: ')

    def setAuthor(self, user):
        author = user
    
    class Meta:
        model = Recipe
        fields = ('name', 'category', 'cuisine', 'image')