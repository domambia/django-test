from django.test import TestCase

from app.calc import add


class CalcTest(TestCase):

    def test_add_two_numbers(self):
        """Test to numbers added together"""
        self.assertEqual(add(3, 8), 11)
