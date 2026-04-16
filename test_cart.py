import unittest
from cart import ShoppingCart

class TestCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()

    def test_add(self):
        self.cart.add_item("apple", 10, 2)
        self.assertEqual(self.cart.get_total(), 20)

    def test_add_same(self):
        self.cart.add_item("apple", 10, 2)
        self.cart.add_item("apple", 10, 3)
        self.assertEqual(self.cart.get_item_count(), 5)

    def test_invalid_qty(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("apple", 10, 0)

    def test_remove(self):
        self.cart.add_item("apple", 10, 1)
        self.cart.remove_item("apple")
        self.assertEqual(self.cart.get_total(), 0)

    def test_discount(self):
        self.cart.add_item("apple", 50, 1)
        self.cart.apply_discount("SAVE10")
        self.assertEqual(self.cart.get_total(), 45)
