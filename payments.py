class PaymentProcessor:
    def __init__(self):
        self.payment_successful = False
        
    def process_payment(self, cart, customer_info):
        """
        Обрабатывает платеж и при успехе очищает корзину
        """
        # В реальной системе здесь была бы интеграция с платежным шлюзом
        total_amount = cart.calculate_total_price()
        
        # Имитация проверки оплаты
        if total_amount > 0 and customer_info.get('name') and customer_info.get('address'):
            self.payment_successful = True
            cart.clear()  # Очищаем корзину после успешной оплаты
            return {"success": True, "message": "Payment processed successfully"}
        else:
            self.payment_successful = False
            return {"success": False, "message": "Payment failed"}