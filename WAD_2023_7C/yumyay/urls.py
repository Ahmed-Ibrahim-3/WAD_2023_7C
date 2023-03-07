from django.urls import path
from yumyay import views
from yumyay.views import LikeRecipeView, UnlikeRecipeView, HasUserLikedRecipe

#  app urls

app_name = 'yumyay'
urlpatterns = [
    path('', views.home, name='home'),
    path('account/', views.account, name='account'),
    path('account/login/', views.log_in, name='log_in'),
    path('account/register/', views.register, name='register'),
    path('cooking/', views.cooking, name='cooking'),
    path('baking/', views.baking, name='baking'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('cooking/cuisine/', views.cuisine, name='cooking_cuisine'),
    path('cooking/cuisine/recipe/', views.recipe_cooking, name='recipe'),
    path('baking/cuisine/recipe/', views.recipe_baking, name='recipe'),
    path('like_recipe/', views.LikeRecipeView.as_view(), name='like_recipe'),
    path('unlike_recipe/', views.UnlikeRecipeView.as_view(), name='unlike_recipe'),
    path('has_user_liked_recipe/', views.HasUserLikedRecipe.as_view(), name='has_user_liked_recipe')
]
