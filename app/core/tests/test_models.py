from django.test import TestCase 
from django.contrib.auth import get_user_model # from user manager


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email       = "test@omambia.com"
        password    = "passwd123"
        user        = get_user_model().objects.create_user(
                    email   = email,
                    password = password
        ) 
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test for new user email is normalized"""
        email  = "textkenya@Email.com"
        user  = get_user_model().objects.create_user(email, "password1232")
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises a value error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "password123")

    def test_create_new_super_user(self):
        """Creating super user"""
        user = get_user_model().objects.create_user(
            email = "super@email.com",
            password = "password123"
        )
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

   