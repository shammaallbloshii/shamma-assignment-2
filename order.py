from shopping_cart import ShoppingCart


class Order:
    """Represents a customer's order."""

    def __init__(self, order_id, customer_id, shopping_cart, shipping_address):
        self.__order_id = order_id
        self.__customer_id = customer_id
        self.__shopping_cart = shopping_cart
        self.__shipping_address = shipping_address
        self.__order_date = "2024-10-29"
        self.__order_total = self.__shopping_cart.calculate_total()

    def place_order(self):
        """Places an order and confirms it."""
        return f"Order {self.__order_id} placed successfully. Total: ${self.__order_total:.2f}"

    def cancel_order(self):
        """Cancels the order."""
        return f"Order {self.__order_id} has been canceled."

    def display_order_details(self):
        """Displays details of the order."""
        return f"Order ID: {self.__order_id}, Total: ${self.__order_total:.2f}, Date: {self.__order_date}"

    def __str__(self):
        return f"Order ID: {self.__order_id}, Customer ID: {self.__customer_id}"
