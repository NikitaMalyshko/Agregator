class Supplier:
    def __init__ (self, name, inn, contact, rating):
        self.name = name
        self.inn = inn
        self.contact = contact
        self.rating = rating
        self.orders = []

    def add_order(self, order_number):
        self.orders.append(order_number)

    def change_rating (self, new_rating):
        if 0 <= new_rating <= 5:
            self.rating = new_rating
        else:
            raise ValueError('Рейтинг должен быть от 0 до 5')

    def display_info(self):
        print("-" * 30 + f"\nПоставщик\nИмя: {self.name},\nИНН: {self.inn},\nКонтакт: {self.contact},\nРейтинг: {self.rating}\n" + "-" * 30)