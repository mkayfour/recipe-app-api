"""
Sample Test
"""

from django.test import SimpleTestCase

from app import calc


class Calctest(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subs_numbers(self):
        """Test subs numbers."""

        res = calc.subs(6, 5)

        self.assertEqual(res, 1)
