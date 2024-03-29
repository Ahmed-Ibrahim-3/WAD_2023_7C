import os
import re
import importlib
import yumyay.forms
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
from yumyay.models import Cuisine, UserProfile, Recipe
from django.core.files.uploadedfile import SimpleUploadedFile
from django.forms import fields as django_fields
from yumyay.forms import *

# Create your tests here.

class PreValidationProjectStructure(TestCase):

    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.static_dir = os.path.join(self.project_base_dir, "static")
        self.media_dir = os.path.join(self.project_base_dir, "media")

    def test_yumyay_python_views_existence(self):
        is_yumyay = os.path.isdir(os.path.join(os.getcwd(), "yumyay"))
        is_python = os.path.isfile(os.path.join(os.path.join(os.getcwd(), "yumyay"), "__init__.py"))
        is_views = os.path.isfile(os.path.join(os.path.join(os.getcwd(), "yumyay"), "views.py"))

        self.assertTrue(is_yumyay)
        self.assertTrue(is_python)
        self.assertTrue(is_views)

    def test_template_directory_existence(self):
        is_template_dir = os.path.join(os.getcwd(), "templates")

        self.assertTrue(is_template_dir)

    def test_static_directory_existence(self):
        is_static_dir = os.path.join(os.getcwd(), "static")

        self.assertTrue(is_static_dir)

    def test_javascript_directory_existence(self):
        is_javascript_dir = os.path.join(os.path.join(os.getcwd(), "templates"), "javascript")

        self.assertTrue(is_javascript_dir)

    def test_css_directory_existence(self):
        is_css_dir = os.path.join(os.path.join(os.getcwd()), "templates", "css")

        self.assertTrue(is_css_dir)

    def test_media_directory_existence(self):
        is_media_dir = os.path.join(os.getcwd(), "media")

        self.assertTrue(is_media_dir)

    def test_yumyay_template_sub_directory(self):
        is_yumyay_sub = os.path.join(os.path.join(os.getcwd(), "templates"), "yumyay")

        self.assertTrue(is_yumyay_sub)

    def test_population_script_existence(self):
        is_population_script = os.path.isfile("populate_script.py")

        self.assertTrue(is_population_script)

    def test_images_directory_existence(self):
        is_images_dir = os.path.join(os.path.join(os.getcwd()), "templates", "images")

        self.assertTrue(is_images_dir)

    def test_population_data_exitsence(self):
        is_population_data = os.path.isfile("populate_data.py")

        self.assertTrue(is_population_data)

    def test_static_and_media_implementations(self):
        static_dir_exists_settings = "STATIC_DIR" in dir(settings)
        self.assertTrue(static_dir_exists_settings)

        expected_path = os.path.normpath(self.static_dir)
        static_path = os.path.normpath(settings.STATIC_DIR)
        self.assertEqual(expected_path, static_path)

        staticfiles_dirs_exists = "STATICFILES_DIRS" in dir(settings)
        self.assertTrue(staticfiles_dirs_exists)
        self.assertEqual([static_path], settings.STATICFILES_DIRS)

        staticfiles_dirs_exists = "STATIC_URL" in dir(settings)
        self.assertTrue(staticfiles_dirs_exists)
        self.assertEqual("/static/", settings.STATIC_URL)

        media_dir_exists = 'MEDIA_DIR' in dir(settings)
        self.assertTrue(media_dir_exists)

        expected_path = os.path.normpath(self.media_dir)
        media_path = os.path.normpath(settings.MEDIA_DIR)
        self.assertEqual(expected_path, media_path)

        media_root_exists = "MEDIA_ROOT" in dir(settings)
        self.assertTrue(media_root_exists)

        media_root_path = os.path.normpath(settings.MEDIA_ROOT)
        self.assertEqual(media_path, media_root_path)

        media_url_exists = "MEDIA_URL" in dir(settings)
        self.assertTrue(media_url_exists)

        media_url_value = settings.MEDIA_URL
        self.assertEqual("/media/", media_url_value)


class TestHomePage(TestCase):

    def setUp(self):
        self.base_dir = os.getcwd()
        self.template_dir = os.path.join(self.base_dir, 'templates', 'yumyay')
        self.about_response = self.client.get(reverse('yumyay:home'))

    def test_successful_deployment(self):
        response = self.client.get(reverse("yumyay:home"))
        self.assertEqual(response.status_code, 200)

    def test_guest_home(self):
        response = self.client.get(reverse("yumyay:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Log in")

    def test_guest_home_2(self):
        response = self.client.get(reverse("yumyay:home"))
        self.assertNotEquals(response.status_code, 404)
        self.assertNotContains(response, "Log out")

    def test_template_home_exists(self):
        template_check = os.path.isfile(os.path.join(os.path.join(os.getcwd(), "templates", "yumyay"), "home.html"))

        self.assertTrue(template_check)

    def test_template_home_usage(self):
        self.assertTemplateUsed(self.about_response, "yumyay/home.html")

    def test_home_page_template_usage(self):
        response = self.client.get(reverse("yumyay:home"))

        self.assertTemplateUsed(response, 'yumyay/home.html')

    def test_home_page_contains_nav_bar(self):
        response = self.client.get(reverse("yumyay:home"))

        self.assertContains(response, "<nav")

    def test_home_page_nav_bar_items(self):
        response = self.client.get(reverse("yumyay:home"))

        self.assertContains(response, "<nav")
        self.assertContains(response, "Home")
        self.assertContains(response, "Cooking")
        self.assertContains(response, "Baking")
        self.assertContains(response, "Account")
        self.assertContains(response, "</nav>")
    
    def test_side_buttons(self):
        response = self.client.get(reverse("yumyay:home"))

        self.assertContains(response, "<button")
        self.assertContains(response, "</button>")
    
    
    
    def test_login_exists(self):
        response = self.client.get(reverse("yumyay:home"))

        self.assertContains(response, "<a")
        self.assertContains(response, "Log in")
        self.assertContains(response, "</a>")

    def create_user(self):
        self.user = User.objects.create_user(
            username="usertest",
            password="mypassword"
        )

    def test_user_login_success(self):
        self.client.login(
            username="usertest",
            password="mypassword"
        )

        response = self.client.get(reverse("yumyay:home"))

        self.assertEqual(response.status_code, 200)

    def test_logged_out_frame(self):
        response = self.client.get(reverse("yumyay:home"))
        response_body = response.content.decode()

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)
        self.assertTrue("Log in" in response_body)


class TestCookingPage(TestCase):

    def setUp(self):
        self.base_dir = os.getcwd()
        self.template_dir = os.path.join(self.base_dir, "templates", "yumyay")
        self.about_response = self.client.get(reverse("yumyay:cooking"))

    def test_successful_deployment(self):
        response = self.client.get(reverse("yumyay:cooking"))
        self.assertEqual(response.status_code, 200)

    def test_guest_cooking(self):
        response = self.client.get(reverse("yumyay:cooking"))
        self.assertEqual(response.status_code, 200)

    def test_template_cooking_exists(self):
        template_check = os.path.isfile(os.path.join(os.path.join(os.getcwd(), "templates", "yumyay"), "cooking.html"))

        self.assertTrue(template_check)

    def test_template_cooking_usage(self):
        self.assertTemplateUsed(self.about_response, "yumyay/cooking.html")

    def test_cooking_page_template_usage(self):
        response = self.client.get(reverse("yumyay:cooking"))

        self.assertTemplateUsed(response, 'yumyay/cooking.html')


class TestAccountPage(TestCase):

    def setUp(self):
        self.base_dir = os.getcwd()
        self.template_dir = os.path.join(self.base_dir, "templates", "yumyay")
        self.about_response = self.client.get(reverse("yumyay:account"))
    
    def test_successful_deployment(self):
        response = self.client.get(reverse("yumyay:account"))

        self.assertEqual(response.status_code, 200)
    
    def test_guest_account(self):
        response = self.client.get(reverse("yumyay:account"))
        
        self.assertEqual(response.status_code, 200)
    
    def test_template_account_exists(self):
        template_check = os.path.isfile(os.path.join(os.path.join(os.getcwd(), "templates", "yumyay"), "account.html"))

        self.assertTrue(template_check)
    
    def test_template_account_usage(self):
        self.assertTemplateUsed(self.about_response, "yumyay/account.html")

    def test_account_page_template_usage(self):
        response = self.client.get(reverse("yumyay:account"))

        self.assertTemplateUsed(response, "yumyay/account.html")
    
    def create_user(self):

        self.user = User.objects.create_user(
            username="usertest",
            password="mypassword"
        )
    
    def test_user_login_success(self):

        self.client.login(
            username="usertest",
            password="mypassword"
        )

        response = self.client.get(reverse("yumyay:account"))

        self.assertEqual(response.status_code, 200)


class TestAddRecipePage(TestCase):

    def setUp(self):
        self.base_dir = os.getcwd()
        self.template_dir = os.path.join(self.base_dir, "templates", "yumyay")
    
    
    def test_template_account_exists(self):
        template_check = os.path.isfile(os.path.join(os.path.join(os.getcwd(), "templates", "yumyay"), "add_recipe.html"))

        self.assertTrue(template_check)


class TestBakingPage(TestCase):

    def setUp(self):
        self.base_dir = os.getcwd()
        self.template_dir = os.path.join(self.base_dir, "templates", "yumyay")
        self.about_response = self.client.get(reverse("yumyay:baking"))
    
    def test_successful_deployment(self):
        
        response = self.client.get(reverse("yumyay:baking"))

        self.assertEqual(response.status_code, 200)
    
    def test_template_account_exists(self):
        template_check = os.path.isfile(os.path.join(os.path.join(os.getcwd(), "templates", "yumyay"), "baking.html"))

        self.assertTrue(template_check)
    
    def test_template_account_usage(self):

        self.assertTemplateUsed(self.about_response, "yumyay/baking.html")

    def test_template_usage(self):
        response = self.client.get(reverse("yumyay:baking"))

        self.assertTemplateUsed(response, "yumyay/baking.html")


class TestLoginPage(TestCase):

    def setUp(self):
        self.base_dir = os.getcwd()
        self.template_dir = os.path.join(self.base_dir, 'templates', 'yumyay')
        self.about_response = self.client.get(reverse('yumyay:log_in'))
    
    def test_successful_deployment(self):
        response = self.client.get(reverse("yumyay:log_in"))

        self.assertEqual(response.status_code, 200)
    
    def test_guest_login(self):
        response = self.client.get(reverse("yumyay:log_in"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Register Here")
        self.assertContains(response, "Don't have an account?")
    
    def test_guest_login_2(self):
        response = self.client.get(reverse("yumyay:home"))

        self.assertNotEquals(response.status_code, 404)
        self.assertNotContains(response, "Log out")
    
    def test_template_login_exists(self):
        template_check = os.path.isfile(os.path.join(os.path.join(os.getcwd(), "templates", "yumyay"), "login.html"))

        self.assertTrue(template_check)
    
    def test_template_login_usage(self):

        self.assertTemplateUsed(self.about_response, "yumyay/login.html")
    
    def test_home_page_template_usage(self):
        response = self.client.get(reverse("yumyay:log_in"))

        self.assertTemplateUsed(response, 'yumyay/login.html')
    
    def test_login_page_contains_form(self):
        response = self.client.get(reverse("yumyay:log_in"))

        self.assertContains(response, "<form")
        self.assertContains(response, "</form>")
    
    def test_login_page_contains_sign_in(self):
        response = self.client.get(reverse("yumyay:log_in"))

        self.assertContains(response, "Sign in")
    
    def test_login_page_contains_input(self):
        response = self.client.get(reverse("yumyay:log_in"))

        self.assertContains(response, '<input type="password"')
        self.assertContains(response, '<input type="text"')
    
    def test_login_page_sign_in_button(self):
        response = self.client.get(reverse("yumyay:log_in"))

        self.assertContains(response, '<button type="submit"')
    
    def create_user(self):
        self.user = User.objects.create_user(
            username="usertest",
            password="mypassword"
        )
    
    def test_user_login_success(self):

        self.client.login(
            username="usertest",
            password="mypassword"
        )

        response = self.client.get(reverse("yumyay:log_in"))

        self.assertEqual(response.status_code, 200)
    
    def test_logged_out_frame(self):
        response = self.client.get(reverse("yumyay:log_in"))
        response_body = response.content.decode()
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Log in" in response_body)


class TestRegisterPage(TestCase):

    def setUp(self):
        self.base_dir = os.getcwd()
        self.template_dir = os.path.join(self.base_dir, 'templates', 'yumyay')
        self.about_response = self.client.get(reverse('yumyay:register'))
    
    def test_successful_deployment(self):
        response = self.client.get(reverse("yumyay:register"))

        self.assertEqual(response.status_code, 200)
    
    def test_guest_register(self):
        response = self.client.get(reverse("yumyay:register"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Register")
    
    def test_guest_register_2(self):
        response = self.client.get(reverse("yumyay:register"))

        self.assertNotEquals(response.status_code, 404)
        self.assertContains(response, "Register")
    
    def test_template_register_exists(self):
        template_check = os.path.isfile(os.path.join(os.path.join(os.getcwd(), "templates", "yumyay"), "register.html"))

        self.assertTrue(template_check)
    
    def test_template_register_usage(self):

        self.assertTemplateUsed(self.about_response, "yumyay/register.html")
    
    def test_register_page_template_usage(self):
        response = self.client.get(reverse("yumyay:register"))

        self.assertTemplateUsed(response, 'yumyay/register.html')
    
    def test_register_page_contains_register(self):
        response = self.client.get(reverse("yumyay:register"))

        self.assertContains(response, "Register")
    
    def test_register_page_contains_form(self):
        response = self.client.get(reverse("yumyay:register"))

        self.assertContains(response, "<form")
        self.assertContains(response, "</form>")
    
    def test_register_page_form_input(self):
        response = self.client.get(reverse("yumyay:register"))

        self.assertContains(response, '<input type="submit"')
    
    def create_user(self):
        self.user = User.objects.create_user(
            username="usertest",
            password="mypassword"
        )
    
    def test_user_login_success(self):
        self.client.login(
            username="usertest",
            password="mypassword"
        )

        response = self.client.get(reverse("yumyay:register"))

        self.assertEqual(response.status_code, 200)
    
    def test_logged_out_frame(self):
        response = self.client.get(reverse("yumyay:register"))
        response_body = response.content.decode()
        
        self.assertEqual(response.status_code, 200)
        self.assertFalse("Log in" in response_body)


class TestModels(TestCase):

    def test_cuisine_name(self):
        cuisine = Cuisine(name = "name1")
        cuisine.save()

        self.assertEqual("name1", cuisine.name)
    
    def test_cuisine_full_model(self):
        cuisine = Cuisine(name = "name1", img = SimpleUploadedFile(
            "cuisine.jpg", b"mock content", content_type="image/jpg"
        ))

        self.assertIsNotNone(cuisine.img)
        self.assertEqual(cuisine.img.name, "cuisine.jpg")
    
    def test_broken_cuisine(self):
        cuisine = Cuisine(name = "name2")
        cuisine.save()

        self.assertNotEqual("name", cuisine.name)
    
    def test_str_cuisine(self):
        cuisine = Cuisine(name="randomcuisine")
        cuisine.save()

        self.assertEqual(str(cuisine), "randomcuisine")
    
    def test_str_recipe(self):
        recipe = Recipe(name="RName")
        recipe.save()

        self.assertEqual(str(recipe), "RName")
    
    
    
    def test_user_model_creation(self):
        sample_user = User.objects.create_user(
            username="test_user",
            password="ThisIsMyPassword"
        )

        self.assertEqual(sample_user.username, "test_user")
        self.assertTrue(sample_user.check_password("ThisIsMyPassword"))
    
    def test_user_model_access_rights(self):
        sample_user = User.objects.create_user(
            username="test_user",
            password="qwerty"
        )

        self.assertFalse(sample_user.is_staff)
        self.assertFalse(sample_user.is_superuser)
    
    def test_super_user_creation(self):
        sample_super_user = User.objects.create_superuser(
            username="super_user",
            password="SuperUser",
            email="email@gmail.com"
        )

        self.assertEqual(sample_super_user.username, "super_user")
        self.assertEqual(sample_super_user.email, "email@gmail.com")
        self.assertTrue(sample_super_user.check_password("SuperUser"))
    
    def test_super_user_access_rights(self):
        sample_super_user = User.objects.create_superuser(
            username="super_user",
            password="IAmASuperUser",
            email="email@gmail.com"
        )

        self.assertTrue(sample_super_user.is_staff)
        self.assertTrue(sample_super_user.is_superuser)
    
    def test_user_profile_model(self):
        test_user_model = User(username = "username", 
                               password = "password")
        test_user_model.save()

        test_user = UserProfile(user=test_user_model,
                                forename = "forename",
                                surname = "surname",
                                emailAddress = "email",
                                password = "password")
        test_user.save()

        self.assertEqual("forename", test_user.forename)
        self.assertEqual("surname", test_user.surname)
        self.assertEqual("email", test_user.emailAddress)
        self.assertEqual("password", test_user.password)
        self.assertEqual(test_user_model, test_user.user)
    
    def test_recipe_model(self):
        test_recipe = Recipe(
            name = "recipe1",
            description = "Recipe Description...",
            ingredients = "Sample Ingredient",
            instructions = "Instructions...",
            category = "B",
            cuisine = "Baking",
            image = SimpleUploadedFile (
                 "recipe.jpg", b"mock content", content_type="image/jpg"
            ),
            likes = 1
        )
        test_recipe.save()

        self.assertEqual("recipe1", test_recipe.name)
        self.assertEqual("Recipe Description...", test_recipe.description)
        self.assertEqual("Sample Ingredient", test_recipe.ingredients)
        self.assertEqual("Instructions...", test_recipe.instructions)
        self.assertEqual("B", test_recipe.category)
        self.assertEqual("Baking", test_recipe.cuisine)
        self.assertIsNotNone(test_recipe.image)
        self.assertEqual(test_recipe.likes, 1)

        test_recipe.likes += 1
        self.assertEqual(test_recipe.likes, 2)
        self.assertNotEqual(test_recipe.likes, 1)
    
    def test_broken_user_profile_model(self):
        test_user_broken_model = User(username = "username_broken", 
                               password = "password_broken")
        test_user_broken_model.save()

        test_user = UserProfile(user=test_user_broken_model,
                                forename = "forename_broken",
                                surname = "surname_broken",
                                emailAddress = "email_broken",
                                password = "password_broken")
        test_user.save()

        self.assertNotEqual("forename", test_user.forename)
        self.assertNotEqual("surname", test_user.surname)
        self.assertNotEqual("email", test_user.emailAddress)
        self.assertNotEqual("password", test_user.password)
    
    def test_profile_model(self):
        user_model = User(username = "username1", 
                               password = "password1")
        user_model.save()

        test_user = UserProfile(user=user_model,
                                forename = "userForename",
                                surname = "userSurname",
                                emailAddress = "emailAddress",
                                password = "password1")
        test_user.save()

        self.assertEqual("userForename", test_user.forename)
        self.assertEqual("userSurname", test_user.surname)
        self.assertEqual("emailAddress", test_user.emailAddress)
        self.assertEqual("password1", test_user.password)
        self.assertEqual(user_model, test_user.user)
    
    def test_broken_recipe_model(self):
        test_broken_recipe = Recipe(
            name = "broken name",
            description = "Broken Description",
            ingredients = "Wrong Ingredients",
            instructions = "Instructions...False",
            category = "C",
            cuisine = "Cooking",
            image = SimpleUploadedFile (
                 "recipe2.jpg", b"mock2 content", content_type="image/jpg"
            ),
            likes = 0
        )
        test_broken_recipe.save()

        self.assertNotEqual("recipe1", test_broken_recipe.name)
        self.assertNotEqual("Recipe Description...", test_broken_recipe.description)
        self.assertNotEqual("Sample Ingredient", test_broken_recipe.ingredients)
        self.assertNotEqual("Instructions...", test_broken_recipe.instructions)
        self.assertNotEqual("B", test_broken_recipe.category)
        self.assertNotEqual("Baking", test_broken_recipe.cuisine)
        self.assertIsNotNone(test_broken_recipe.image)
        self.assertNotEqual(test_broken_recipe.likes, 1)

        test_broken_recipe.likes += 1
        self.assertNotEqual(test_broken_recipe.likes, 2)
        self.assertEqual(test_broken_recipe.likes, 1)


class TestLoginFunctionality(TestCase):

    def test_log_in_exists(self):

        url = ''

        try:
            url = reverse('yumyay:log_in')
        except:
            pass

        self.assertEqual(url, '/yumyay/account/login/')
    
    def test_successful_login(self):
        user = User.objects.get_or_create(username='testuser',
                                      first_name='firstName',
                                      last_name='lastName',
                                      email='test@gmail.com')[0]
        
        user.set_password('passwordTest')
        user.save()


        user_object = user

        response = self.client.post(reverse('yumyay:log_in'), {'username': 'testuser', 'password': 'passwordTest'})
        
        try:
            self.assertEqual(user_object.id, int(self.client.session['_auth_user_id']))
        except KeyError:
            self.assertTrue(False)

        self.assertEqual(response.status_code, 302)
    
    def test_unsucessful_login(self):
        user = User.objects.get_or_create(username='testuser',
                                      first_name='firstName',
                                      last_name='lastName',
                                      email='test@gmail.com')[0]
        
        user.set_password('passwordTest')
        user.save()

        user_object = user

        
        try:
            self.assertNotEqual(user_object.id, int(self.client.session['_auth_user_id']))
        except KeyError:
            self.assertFalse(False)

    def test_login_template_usage(self):
        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'yumyay')
        template_path = os.path.join(template_base_path, 'login.html')

        self.assertTrue(os.path.exists(template_path))

        f = open(template_path, 'r')
        template_str = ""
        
        for line in f:
           template_str = f"{template_str}{line}"

        f.close()

        full_title_pattern = r'<title>(\s*|\n*)yumyay(\s*|\n*)-(\s*|\n*)Login(\s*|\n*)</title>'

        block_title_pattern = r'{% block title_block %}(\s*|\n*)Login(\s*|\n*){% (endblock|endblock title_block) %}'

        request_pattern = self.client.get(reverse('yumyay:log_in'))
        content_pattern = request_pattern.content.decode('utf-8')

        self.assertTrue(re.search(full_title_pattern, content_pattern))

        self.assertTrue(re.search(block_title_pattern, template_str))
    
    def test_restricted_url_exists(self):

        url = ''

        try:
            url = reverse('yumyay:edit_details')
        except:
            pass
        
        self.assertEqual(url, '/yumyay/account/edit_details/')


class LogoutFunctionalityTests(TestCase):
    
    def test_bad_request(self):
        
        response = self.client.get(reverse('yumyay:log_in'))

        self.assertTrue(response.status_code, 302)

        self.assertNotEqual(response, reverse('yumyay:log_out')) 
    
    def test_good_request(self):

        user = User.objects.get_or_create(username='testuser',
                                      first_name='Test',
                                      last_name='User',
                                      email='test@test.com')[0]
        
        user.set_password('testabc123')
        user.save()


        user_object = user

        self.client.login(username='testuser', password='testabc123')

        try:
            self.assertEqual(user_object.id, int(self.client.session['_auth_user_id']))
        except KeyError:
            self.assertTrue(False)
        
        response = self.client.get(reverse('yumyay:log_out'))

        self.assertEqual(response.status_code, 302)

        self.assertEqual(response.url, reverse('yumyay:home'))

        self.assertTrue('_auth_user_id' not in self.client.session)


class ViewTests(TestCase):

    def setUp(self):

        self.views_module = importlib.import_module("yumyay.views")

        self.views_module_directory = dir(self.views_module)
        
        self.project_urls_module = importlib.import_module('WAD_2023_7C.urls')

    def test_home_view_exists(self):
        home_view_exists = "home" in self.views_module_directory
        is_callable = callable(self.views_module.home)

        self.assertTrue(home_view_exists)

        self.assertTrue(is_callable)
    
    def test_home_view_mapping(self):
        home_mapping_existence = False

        for mapping in self.project_urls_module.urlpatterns:
            if hasattr(mapping, "name"):
                if mapping.name == "home":
                    home_mapping_existence = True
        

        self.assertTrue(home_mapping_existence)
        self.assertEquals(reverse("yumyay:home"), "/yumyay/")
    
    def test_log_in_view_exists(self):
        log_in_view_exists = "log_in" in self.views_module_directory
        is_callable = callable(self.views_module.home)

        self.assertTrue(log_in_view_exists)
        self.assertTrue(is_callable)
    
    def test_log_in_view_mapping(self):

        self.assertEquals(reverse("yumyay:log_in"), "/yumyay/account/login/")

    def test_account_view_exists(self):
        account_view_exists = "account" in self.views_module_directory
        is_callable = callable(self.views_module.home)

        self.assertTrue(account_view_exists)
        self.assertTrue(is_callable)
    
    def test_account_view_mapping(self):

        self.assertEquals(reverse("yumyay:account"), "/yumyay/account/")

    def test_cooking_view_exists(self):
        cooking_view_exists = "cooking" in self.views_module_directory
        is_callable = callable(self.views_module.home)

        self.assertTrue(cooking_view_exists)
        self.assertTrue(is_callable)
    
    def test_cooking_view_mapping(self):

        self.assertEquals(reverse("yumyay:cooking"), "/yumyay/cooking/")
    
    def test_baking_view_exists(self):
        baking_view_exists = "baking" in self.views_module_directory
        is_callable = callable(self.views_module.home)

        self.assertTrue(baking_view_exists)
        self.assertTrue(is_callable)
    
    def test_baking_view_mapping(self):

        self.assertEquals(reverse("yumyay:baking"), "/yumyay/baking/")
    
    def test_add_recipe_exists(self):
        add_recipe_view_exists = "add_recipe" in self.views_module_directory
        is_callable = callable(self.views_module.home)

        self.assertTrue(add_recipe_view_exists)

        self.assertTrue(is_callable)
    
    def test_add_recipe_view_mapping(self):

        self.assertEquals(reverse("yumyay:add_recipe"), "/yumyay/add_recipe/")
    
    def test_register_view_exists(self):
        recipe_view_exists = "register" in self.views_module_directory
        is_callable = callable(self.views_module.home)

        self.assertTrue(recipe_view_exists)

        self.assertTrue(is_callable)
    
    def test_register_view_mapping(self):

        self.assertEquals(reverse("yumyay:register"), "/yumyay/account/register/")

    
    def test_edit_details_view_exists(self):
        edit_details_view_exists = "edit_details" in self.views_module_directory
        is_callable = callable(self.views_module.home)

        self.assertTrue(edit_details_view_exists)

        self.assertTrue(is_callable)
    
    def test_edit_details_view_mapping(self):

        self.assertEquals(reverse("yumyay:edit_details"), "/yumyay/account/edit_details/")
    
    def test_delete_recipe_view_exists(self):
        delete_recipe_view_exists = "delete_recipe" in self.views_module_directory
        is_callable = callable(self.views_module.home)

        self.assertTrue(delete_recipe_view_exists)
        self.assertTrue(is_callable)
    
    def test_user_login_view_exists(self):
        user_login_view_exists = "user_login" in self.views_module_directory
        is_callable = callable(self.views_module.home)

        self.assertTrue(user_login_view_exists)
        self.assertTrue(is_callable)
    
    def test_user_login_view_mapping(self):
        
        self.assertEquals(reverse("yumyay:log_in"), "/yumyay/account/login/")
    
    def test_user_logout_view_exists(self):
        user_logout_view_exists = "user_logout" in self.views_module_directory
        is_callable = callable(self.views_module.home)

        self.assertTrue(user_logout_view_exists)

        self.assertTrue(is_callable)
    
    def test_user_logout_view_mapping(self):

        self.assertEquals(reverse("yumyay:log_out"), "/yumyay/account/logout/")
    
    def test_recipe_view_exists(self):
        recipe_view_exists = "recipe" in self.views_module_directory
        is_callable = callable(self.views_module.home)

        self.assertTrue(recipe_view_exists)

        self.assertTrue(is_callable)
    

    def test_cuisine_view_exists(self):
        cuisine_view_exists = "cuisine" in self.views_module_directory
        is_callable = callable(self.views_module.home)

        self.assertTrue(cuisine_view_exists)
        self.assertTrue(is_callable)
    
    def test_like_view_exists(self):
        like_view_exists = "LikeRecipeView" in self.views_module_directory
        is_callable = callable(self.views_module.home)

        self.assertTrue(like_view_exists)

        self.assertTrue(is_callable)
    
    def test_liked_view_exists(self):
        like_view_exists = "HasUserLikedRecipe" in self.views_module_directory
        is_callable = callable(self.views_module.home)

        self.assertTrue(like_view_exists)
        self.assertTrue(is_callable)
    
    def test_delete_view_exists(self):
        delete_view_exists = "delete" in self.views_module_directory
        is_callable = callable(self.views_module.home)

        self.assertTrue(delete_view_exists)

        self.assertTrue(is_callable)
    
    def test_second_logout_url_mapping(self):
        self.assertEquals(reverse("yumyay:logout"), "/yumyay/logout/")


class TestForms(TestCase):

    def test_forms_file_exists(self):
        file_path = os.getcwd()
        yumyay_app = os.path.join(file_path, "yumyay")
        yumyay_forms_path = os.path.join(yumyay_app, "forms.py")

        self.assertTrue(os.path.exists(yumyay_forms_path))
    
    def test_recipe_form_class(self):
        self.assertTrue("RecipeForm" in dir(yumyay.forms))

        recipe_form = RecipeForm()
        self.assertEqual(type(recipe_form.__dict__["instance"]), Recipe)

        fields = recipe_form.fields

        form_fields = {
            "name" : django_fields.CharField,
            "description" : django_fields.CharField,
            "ingredients" : django_fields.CharField,
            "instructions" : django_fields.CharField,
            "category" : django_fields.ChoiceField,
            "cuisine" : django_fields.TypedChoiceField,
            "image" : django_fields.ImageField,
        }

        for entry in form_fields:
            confirm_field = form_fields[entry]
    
            self.assertTrue(entry in fields.keys())
            
            self.assertEquals(confirm_field, type(fields[entry]))
    
    def test_user_form_class(self):
        self.assertTrue("UserForm" in dir(yumyay.forms))

        user_form = UserForm()

        self.assertEqual(type(user_form.__dict__["instance"]), User)

        fields = user_form.fields

        form_fields = {
            "username" : django_fields.CharField,
            "first_name" : django_fields.CharField,
            "last_name" : django_fields.CharField,
            "email" : django_fields.EmailField,
            "password" : django_fields.CharField
        }

        for entry in form_fields:
            confirm_field = form_fields[entry]

            self.assertTrue(entry in fields.keys())
            self.assertEqual(confirm_field, type(fields[entry]))
    
    def test_edit_details_form(self):
        self.assertTrue("EditDetailsForm" in dir(yumyay.forms))

        edit_form = EditDetailsForm()

        self.assertEqual(type(edit_form.__dict__["instance"]), User)

        fields = edit_form.fields

        form_fields = {
            "first_name" : django_fields.CharField,
            "last_name" : django_fields.CharField,
            "email" : django_fields.EmailField
        }

        for entry in form_fields:
            confirm_field = form_fields[entry]

            self.assertTrue(entry in fields.keys())
            self.assertEqual(confirm_field, type(fields[entry]))
   

