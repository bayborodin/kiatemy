from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class ViewTestCase(TestCase):
    """Test suite for the api views"""

    def setUp(self):
        """Define the test client and other variables."""
        self.client = APIClient()
        self.account_data = {"name": "Test account"}

    def test_api_can_create_an_account(self):
        """Test the api has account creation capability."""
        response = self.client.post(
            reverse("accounts-list"),
            self.account_data,
            format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
