from django.test import TestCase
from .views import generate_password
import string

class GeneratorTests(TestCase):
    def test_length(self):
        p = generate_password(8)
        self.assertEqual(len(p), 8)

    def test_digits_presence(self):
        p = generate_password(12, use_digits=True, use_symbols=False, use_upper=False)
        self.assertTrue(any(c in string.digits for c in p))

    def test_only_lowercase_when_others_off(self):
        p = generate_password(10, use_upper=False, use_digits=False, use_symbols=False)
        for c in p:
            self.assertIn(c, string.ascii_lowercase)
