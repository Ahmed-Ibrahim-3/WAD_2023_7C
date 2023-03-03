from django.test import TestCase
from django.urls import reverse

# Create your tests here.

#Commented Tests on Purpose - waiting for migrations of models.
'''class TestHomePageLoggedOut(TestCase):

    def test_successful_deployment(self):
        response = self.client.get(reverse("yumyay:home"))
        self.assertEqual(response.status_code, 200)

    def test_guest_home(self):
        response = self.client.get(reverse("yumyay:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Log in")
    
    def test_guest_home_2(self):
        response = self.client.get(reverse("yumyay:home"))
        self.assertFalse(response.status_code, 404)
        self.assertNotContains(response, "Log out")'''