class Material:
    def __init__ (self, title, price, unit="шт"):
        self.title = title
        self.price = price
        self.unit = unit

    def display_info(self):
        print(f"Товар: {self.title} | Цена: {self.price} руб./{self.unit}")