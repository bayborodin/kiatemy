from django.test import TestCase
from django.contrib.auth import get_user_model


class Modeltests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "test@kiatemy.local"
        password = "Testpass123"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "test@KIATEMY.LOCAL"
        user = get_user_model().objects.create_user(email, "test123")

        self.assertEquals(user.email, email.lower())