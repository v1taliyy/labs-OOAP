from abc import ABC, abstractmethod


# Базовий клас виробу
class Jewelry(ABC):
    def __init__(self, name, metal, weight, complexity, work_price_per_unit, metal_price_per_gram):
        self.name = name
        self.metal = metal
        self.weight = weight
        self.complexity = complexity
        self.work_price_per_unit = work_price_per_unit
        self.metal_price_per_gram = metal_price_per_gram

    # розрахунок ціни: матеріал + робота
    def calculate_price(self):
        material_price = self.weight * self.metal_price_per_gram
        work_price = self.complexity * self.work_price_per_unit
        return material_price + work_price

    def info(self):
        return (
            f"{self.name} | {self.metal} | "
            f"{self.weight} г | складність {self.complexity} | "
            f"{self.calculate_price():.2f} грн"
        )


# Абстрактна фабрика
class JewelryFactory(ABC):
    @abstractmethod
    def create_earrings(self, weight, complexity):
        pass

    @abstractmethod
    def create_ring(self, weight, complexity):
        pass

    @abstractmethod
    def create_chain(self, weight, complexity):
        pass

    @abstractmethod
    def create_pendant(self, weight, complexity):
        pass

    @abstractmethod
    def create_bracelet(self, weight, complexity):
        pass


# Фабрика золота
class GoldFactory(JewelryFactory):
    METAL = "Золото"
    METAL_PRICE = 3200
    WORK_PRICE = 500  # однакова для золота і срібла

    def create_earrings(self, weight, complexity):
        return JewelryItem("Сережки", self.METAL, weight, complexity, self.WORK_PRICE, self.METAL_PRICE)

    def create_ring(self, weight, complexity):
        return JewelryItem("Каблучка", self.METAL, weight, complexity, self.WORK_PRICE, self.METAL_PRICE)

    def create_chain(self, weight, complexity):
        return JewelryItem("Ланцюжок", self.METAL, weight, complexity, self.WORK_PRICE, self.METAL_PRICE)

    def create_pendant(self, weight, complexity):
        return JewelryItem("Підвіска", self.METAL, weight, complexity, self.WORK_PRICE, self.METAL_PRICE)

    def create_bracelet(self, weight, complexity):
        return JewelryItem("Браслет", self.METAL, weight, complexity, self.WORK_PRICE, self.METAL_PRICE)


# Фабрика срібла
class SilverFactory(JewelryFactory):
    METAL = "Срібло"
    METAL_PRICE = 1200
    WORK_PRICE = 500  # така сама як і для золота

    def create_earrings(self, weight, complexity):
        return JewelryItem("Сережки", self.METAL, weight, complexity, self.WORK_PRICE, self.METAL_PRICE)

    def create_ring(self, weight, complexity):
        return JewelryItem("Каблучка", self.METAL, weight, complexity, self.WORK_PRICE, self.METAL_PRICE)

    def create_chain(self, weight, complexity):
        return JewelryItem("Ланцюжок", self.METAL, weight, complexity, self.WORK_PRICE, self.METAL_PRICE)

    def create_pendant(self, weight, complexity):
        return JewelryItem("Підвіска", self.METAL, weight, complexity, self.WORK_PRICE, self.METAL_PRICE)

    def create_bracelet(self, weight, complexity):
        return JewelryItem("Браслет", self.METAL, weight, complexity, self.WORK_PRICE, self.METAL_PRICE)


# Конкретний виріб
class JewelryItem(Jewelry):
    pass


# Каталог виробів
class Catalog:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    # перегляд по категорії (золото / срібло)
    def show_by_category(self, metal):
        print(f"\n=== {metal} ===")
        for item in self.items:
            if item.metal == metal:
                print(item.info())


def main():
    gold_factory = GoldFactory()
    silver_factory = SilverFactory()

    catalog = Catalog()

    # створення виробів через фабрики
    catalog.add_item(gold_factory.create_earrings(4.5, 2))
    catalog.add_item(gold_factory.create_ring(3.2, 3))
    catalog.add_item(gold_factory.create_chain(8.0, 4))

    catalog.add_item(silver_factory.create_earrings(4.5, 2))
    catalog.add_item(silver_factory.create_pendant(2.1, 1))
    catalog.add_item(silver_factory.create_bracelet(6.3, 3))

    # перегляд каталогу
    catalog.show_by_category("Золото")
    catalog.show_by_category("Срібло")


if __name__ == "__main__":
    main()