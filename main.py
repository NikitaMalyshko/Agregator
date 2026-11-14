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

class Request:
    def __init__ (self, item_name, supplier, quantity, price):
        self.item_name = item_name
        self.supplier = supplier
        self.quantity = quantity
        self.price = price

    def calculate_total(self): # Считает общую сумму
        return self.quantity * self.price

    def send(self):
        print("-" * 30 + f"\nЗаявка на '{self.item_name}' была успешно отправлена!")
        print(f"Поставщик: {self.supplier.name}")
        print(f"Контакт для связи: {self.supplier.contact}\n" + "-" * 30)

tgl = Supplier("ЗАО Террагрупп лабс", "7621234657", "zakaz@tglabs.com", 4.8)
tgl.add_order("PO-001")
tgl.display_info()
print("Заказы tgl: ", tgl.orders)

req_1 = Request("Графитовый блок", tgl)
req_1.send()

