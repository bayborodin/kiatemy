from django.test import TestCase

from account.models import Account


class AccountTests(TestCase):
    """This class defines the test suite for the Account model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.account_name = "Test account"
        self.account = Account(name=self.account_name)

    def test_model_can_create_an_account(self):
        """Test the Account model can create an Account entity."""
        old_count = Account.objects.count()
        self.account.save()
        new_count = Account.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_account_string_representation(self):
        """Test Account string representation"""
        self.account.save()
        self.assertEqual(str(self.account), self.account.name)
