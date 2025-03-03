import unittest
from cart import Cart
from payments import PaymentProcessor

class TestCartPaymentIntegration(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.payment_processor = PaymentProcessor()
        
    def test_successful_payment_clears_cart(self):
        # Добавляем товары в корзину
        self.cart.add_item(1, "Python Programming", 29.99)
        self.cart.add_item(2, "Data Science Handbook", 39.99)
        
        # Проверяем, что в корзине есть товары
        self.assertEqual(len(self.cart.get_items()), 2)
        
        # Осуществляем оплату
        customer_info = {
            "name": "John Doe",
            "address": "123 Main St, City"
        }
        
        result = self.payment_processor.process_payment(self.cart, customer_info)
        
        # Проверяем, что оплата успешна
        self.assertTrue(result["success"])
        
        # Проверяем, что корзина очищена после успешной оплаты
        self.assertEqual(len(self.cart.get_items()), 0)
        
    def test_failed_payment_keeps_cart_items(self):
        # Добавляем товары в корзину
        self.cart.add_item(1, "Python Programming", 29.99)
        
        # Недостаточно данных для успешной оплаты
        customer_info = {
            "name": "John Doe"
            # Отсутствует адрес
        }
        
        result = self.payment_processor.process_payment(self.cart, customer_info)
        
        # Проверяем, что оплата не прошла
        self.assertFalse(result["success"])
        
        # Проверяем, что товары остались в корзине
        self.assertEqual(len(self.cart.get_items()), 1)

if __name__ == '__main__':
    unittest.main()