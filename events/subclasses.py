from .log_event import LogEvent

#Subclase ProductViewEvent. Campos: product_id, product_name
class ProductViewEvent(LogEvent):
    def __init__(self, *, product_id: int, product_name: str, **kwargs):
        super().__init__(event_type="product_view", **kwargs)
        self.product_id = product_id
        self.product_name = product_name

#Subclase AddToCartEvent. Campos: product_id, quantity, price
class AddToCartEvent(LogEvent):
    def __init__(self, *, product_id: int, quantity: int, price: float, **kwargs):
        super().__init__(event_type="add_to_cart", **kwargs)
        self.product_id = product_id
        self.quantity = quantity
        self.price = price