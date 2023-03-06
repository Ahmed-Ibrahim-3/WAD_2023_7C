import os
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.

class PreValidationProjectStructure(TestCase):

    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.static_dir = os.path.join(self.project_base_dir, "static")
        self.media_dir = os.path.join(self.project_base_dir, "media")

    def test_yumyay_python_views_existence(self):
        is_yumyay = os.path.isdir(os.path.join(os.getcwd(), "yumyay"))
        is_python = os.path.isfile(os.path.join(os.path.join(os.getcwd(), "yumyay"),"__init__.py"))
        is_views = os.path.isfile(os.path.join(os.path.join(os.getcwd(), "yumyay"),"views.py"))

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

    #Not Added - Passed
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