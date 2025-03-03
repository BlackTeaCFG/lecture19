import unittest
from cart import Cart

class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        
    def test_empty_cart_total(self):
        # Проверка, что пустая корзина имеет нулевую стоимость
        self.assertEqual(self.cart.calculate_total_price(), 0)
        
    def test_add_single_item(self):
        # Проверка добавления одного товара
        self.cart.add_item(1, "Python Programming", 29.99)
        self.assertEqual(self.cart.calculate_total_price(), 29.99)
        
    def test_add_multiple_items(self):
        # Проверка добавления нескольких товаров
        self.cart.add_item(1, "Python Programming", 29.99)
        self.cart.add_item(2, "Data Science Handbook", 39.99)
        self.assertEqual(round(self.cart.calculate_total_price(), 2), 69.98)
        
    def test_clear_cart(self):
        # Проверка очистки корзины
        self.cart.add_item(1, "Python Programming", 29.99)
        self.cart.clear()
        self.assertEqual(self.cart.calculate_total_price(), 0)

if __name__ == '__main__':
    unittest.main()