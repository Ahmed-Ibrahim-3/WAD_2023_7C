from django.urls import path
from yumyay import views

#  app urls

app_name = 'yumyay'
urlpatterns = [
    path('', views.home, name='home'),
    path('account/', views.account, name='account'),
    path('account/login/', views.user_login, name='log_in'),
    path('account/logout/', views.user_logout, name='log_out'),
    path('account/delete_user/<str:username>/', views.delete_user, name='delete_user'),
    path('account/register/', views.register, name='register'),
    path('cooking/', views.cooking, name='cooking'),
    path('baking/', views.baking, name='baking'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('baking/<slug:cuisine_name_slug>/', views.cuisine, name='baking_cuisine'),
    path('cooking/<slug:cuisine_name_slug>/', views.cuisine, name='cooking_cuisine'),
    path('cooking/cuisine/recipe/', views.recipe_cooking, name='recipe'),
    path('baking/cuisine/recipe/', views.recipe_baking, name='recipe'),
    path('like_recipe/', views.LikeRecipeView.as_view(), name='like_recipe'),
    path('has_user_liked_recipe/', views.HasUserLikedRecipe.as_view(), name='has_user_liked_recipe'),
    path('logout/', views.user_logout, name='logout'),
]
