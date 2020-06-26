from django.test import TestCase

from account import models


class ModelTests(TestCase):
    def test_create_account(self):
        """Test Account string representation"""
        account = models.Account.objects.create(
            name="Test Account"
        )

        self.assertEqual(str(account), account.name)
