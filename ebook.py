class EBook:
    """Represents an eBook with its details."""

    def __init__(self, book_id, title, author, price, genre, stock_quantity):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__price = price
        self.__genre = genre
        self.__stock_quantity = stock_quantity

    def update_stock(self, quantity):
        """Updates the stock quantity of the eBook."""
        self.__stock_quantity += quantity

    def display_book_info(self):
        """Displays detailed information about the eBook."""
        return f"Title: {self.__title}, Author: {self.__author}, Price: ${self.__price}, Genre: {self.__genre}"

    def apply_discount(self, discount_percentage):
        """Applies a discount to the eBook price."""
        self.__price *= (1 - discount_percentage / 100)

    def get_price(self):
        """Returns the price of the eBook."""
        return self.__price

    def __str__(self):
        return f"ID: {self.__book_id}, Title: {self.__title}, Stock: {self.__stock_quantity}"
