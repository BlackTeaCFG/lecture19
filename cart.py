class Cart:
    def __init__(self):
        self.items = []
    
    def add_item(self, book_id, title, price, quantity=1):
        self.items.append({
            'book_id': book_id,
            'title': title,
            'price': price,
            'quantity': quantity
        })
    
    def calculate_total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.items)
    
    def clear(self):
        self.items = []

    def get_items(self):
        return self.items