class Invoice:
    """Represents the invoice for an order."""

    def __init__(self, invoice_id, order_id, customer_id, amount_paid, invoice_date):
        self.__invoice_id = invoice_id
        self.__order_id = order_id
        self.__customer_id = customer_id
        self.__amount_paid = amount_paid
        self.__invoice_date = invoice_date

    def generate_invoice(self):
        """Generates the invoice details."""
        return f"Invoice ID: {self.__invoice_id}, Order ID: {self.__order_id}, Amount Paid: ${self.__amount_paid:.2f}, Date: {self.__invoice_date}"

    def print_invoice(self):
        """Prints the invoice."""
        print(self.generate_invoice())

    def __str__(self):
        return f"Invoice ID: {self.__invoice_id}, Amount Paid: ${self.__amount_paid:.2f}"
