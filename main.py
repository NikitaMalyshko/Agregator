from models.supplier import Supplier
from models.material import Material
from models.request import Request
from department import Department

# Тестовые данные
def main():
    # 1. Создаем "отдел"
    dept = Department()

    # 2. Создаем объекты (данные)
    tgl = Supplier("ЗАО Террагрупп", "1234567890", "zakaz@tglabs.com", 4.8)
    graphite = Material("Графитовый блок", 1500)

    # 3. Помещаем их в отдел
    dept.suppliers.append(tgl)
    dept.materials.append(graphite)

    # 4. Создаем заявку (взаимодействие объектов)
    req_1 = Request(material=graphite, supplier=tgl, quantity=10)

    # 5. Отправляем и выводим
    req_1.send()

    print("\n--- Информация о поставщиках ---")
    dept.show_all_suppliers()


if __name__ == "__main__":
    main()