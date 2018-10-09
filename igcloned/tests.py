from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from .views import signup
from .forms import SignUpForm


class SignUpTests(TestCase):
    """
    signup tests
    """
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/signup/')
        self.assertEquals(view.func, signup)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, SignUpForm)


class SuccessfulSignUpTests(TestCase):
    """
    successful signup tests
    """
    def setUp(self):
        url = reverse('signup')
        data = {
            'username': 'eugene',
            'email': 'eugenenzioki@gmail.com',
            'password1': 'qwerty123',
            'password2': 'qwerty123'
        }
        self.response = self.client.post(url, data)
        self.edit_profile_url = reverse('edit_profile')

    def test_form_inputs(self):
        """
        testing form input
        :return:
        """
        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="text"', 1)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, 'type="password"', 2)

    def test_redirection(self):
        """
        testing for redirection to profile edit page upon signup
        """
        self.assertRedirects(self.response, self.edit_profile_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        """
        test user authentication

        """
        response = self.client.get(self.edit_profile_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)


# invalid signup tests
class InvalidSignUpTests(TestCase):
    """
    testing for signup
    """
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.post(url, {})  # submit an empty dictionary

    def test_signup_status_code(self):
        """
        testing invalid form submission
        """
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())