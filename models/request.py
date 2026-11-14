from models.supplier import Supplier
from models.material import Material

class Request:
    def __init__(self, material: Material, supplier: Supplier, quantity):
        self.material = material
        self.supplier = supplier
        self.quantity = quantity
        self.status = "Новая"

    def calculate_total(self):
        """Считает общую сумму: перемножает количество на цену из товара"""
        return self.quantity * self.material.price

    def send(self):
        print("-" * 30)
        print(f"Заявка на '{self.material.title}' ({self.quantity} шт.) отправлена!")
        print(f"Поставщик: {self.supplier.name}")
        print(f"Сумма: {self.calculate_total()} руб.")
        print("-" * 30)