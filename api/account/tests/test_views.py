from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from account.models import Account


class ViewTestCase(TestCase):
    """Test suite for the api views"""

    def setUp(self):
        """Define the test client and other variables."""
        self.client = APIClient()
        self.account_data = {"name": "Test account"}
        self.response = self.client.post(
            reverse("accounts-list"), self.account_data, format="json"
        )

    def test_api_can_create_an_account(self):
        """Test the api has account creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_account(self):
        """Test the api can get a given account."""
        account = Account.objects.get()
        response = self.client.get(
            reverse("accounts-detail", kwargs={"pk": account.id}),
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, account)

    def test_api_can_update_account(self):
        """Test the api can update a given account"""
        account = Account.objects.get()
        change_account = {"name": "Something new"}
        res = self.client.put(
            reverse("accounts-detail", kwargs={"pk": account.id}),
            change_account,
            format="json",
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_account(self):
        """Test the api can delete an account"""
        account = Account.objects.get()
        response = self.client.delete(
            reverse("accounts-detail", kwargs={"pk": account.id}),
            format="json",
            follow=True,
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
