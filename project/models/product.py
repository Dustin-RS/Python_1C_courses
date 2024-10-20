class Product:
    def __init__(self, name: str, category: str, price: float):
        """
        Initialize a Product instance.

        :param name: str: The name of the product.
        :param category: str: The category of the product.
        :param price: float: The price of the product.
        """
        self.name: str = name
        self.category: str = category
        self.price: float = price
        self.sale: float = 0

    def edit_category(self, new_category: str):
        """
        Edit the category of the product.

        :param new_category: str: The new category to set.
        """
        self.category = new_category

    def edit_price(self, new_price: float):
        """
        Edit the price of the product.

        :param new_price: float: The new price to set.
        """
        self.price = new_price

    def set_sale(self, sale: float):
        """
        Set a discount (sale) on the product.

        :param sale: float: Discount percentage (0-100).
        """
        if sale < 0 or sale > 100:
            raise ValueError("Sale percentage must be between 0 and 100.")

        self.sale = sale

    def cancel_sale(self):
        """Cancel the current sale and reset the discount to 0%."""
        self.sale = 0

    def get_price(self) -> float:
        """
        Calculate the price after applying the discount.

        :return: The price after the discount is applied.
        """
        if self.sale > 0:
            discount = (self.price * self.sale) / 100
            return self.price - discount
        return self.price

    def __repr__(self) -> str:
        """
        Return a string representation of the product.

        :return: String representation of the product.
        """
        return (
            f"Product(name='{self.name}', category='{self.category}', "
            f"price={self.price}, sale={self.sale}%)"
        )