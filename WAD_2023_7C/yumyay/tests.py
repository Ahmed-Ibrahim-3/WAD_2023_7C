import os
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings


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
        self.assertFalse(response.status_code, 404)
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


class TestTargettedRecipePage(TestCase):

    def setUp(self):
        self.base_dir = os.getcwd()
        self.template_dir = os.path.join(self.base_dir, "templates", "yumyay")
        self.about_response = self.client.get(reverse("yumyay:recipe"))

    def test_successful_deployment(self):
        response = self.client.get(reverse("yumyay:recipe"))

        self.assertEqual(response.status_code, 200)

    def test_template_account_exists(self):
        template_check = os.path.isfile(os.path.join(os.path.join(os.getcwd(), "templates", "yumyay"), "recipe.html"))

        self.assertTrue(template_check)

    def test_template_account_usage(self):
        self.assertTemplateUsed(self.about_response, "yumyay/recipe.html")

    def test_template_usage(self):
        response = self.client.get(reverse("yumyay:recipe"))

        self.assertTemplateUsed(response, 'yumyay/recipe.html')

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