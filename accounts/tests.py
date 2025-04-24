from django.test import TestCase
from  django.contrib.auth import get_user_model
from django.urls import reverse
# Create your tests here.
class UserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='test',
            email='ahmedshehta0123@gmail.com',
            password='12345678'
        )

        self.assertEqual(user.username, 'test')
        self.assertEqual(user.email, 'ahmedshehta0123@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='test',
            email='ahmedshehta0123@gmail.com',
            password='123456789'
        )
        self.assertEqual(user.username, 'test')
        self.assertEqual(user.email, 'ahmedshehta0123@gmail.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class SignupTest(TestCase):
    def test_url_exits_at_correct_location(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_url_view_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)

    def test_signup_form(self):
        response = self.client.post(reverse("signup"),
                                    {
                                        "username": "testuser",
                                        "email": "testuser@email.com",
                                        "password1": "testpass123",
                                        "password2": "testpass123",
                                    },)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, 'testuser')