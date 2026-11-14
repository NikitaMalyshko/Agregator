from models.supplier import Supplier
from models.material import Material
from models.request import Request

class Department:
    def __init__(self):
        # Здесь временно хранится вся "БД" в оперативной памяти
        self.suppliers = []
        self.materials = []
        self.requests = []

    def show_all_suppliers(self):
        if not self.suppliers:
            print("Список поставщиков пуст.")
        for s in self.suppliers:
            s.display_info()