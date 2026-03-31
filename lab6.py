from abc import ABC, abstractmethod


# спільний інтерфейс для всіх елементів карти
class MapComponent(ABC):
    def __init__(self, name, x=0, y=0):
        self.parent = None
        self.name = name
        self._x = x
        self._y = y

    @abstractmethod
    def draw(self, x=0, y=0):
        pass

    # пошук по імені
    def find_child(self, name):
        if self.name == name:
            return self
        return None


# простий елемент карти
class MapObject(MapComponent):
    def draw(self, x=0, y=0):
        real_x = x + self._x
        real_y = y + self._y
        print(f"Об'єкт: {self.name}, координати: ({real_x}, {real_y})")


# складений елемент карти
class MapGroup(MapComponent):
    def __init__(self, name, x=0, y=0):
        super().__init__(name, x, y)
        self.components = []

    # додаємо дочірній елемент
    def add_component(self, component):
        component.parent = self
        self.components.append(component)

    # малюємо групу і всі її дочірні елементи
    def draw(self, x=0, y=0):
        real_x = x + self._x
        real_y = y + self._y
        print(f"\nГрупа: {self.name}, координати: ({real_x}, {real_y})")

        for component in self.components:
            component.draw(real_x, real_y)

    # шукаємо елемент у собі та своїх нащадках
    def find_child(self, name):
        if self.name == name:
            return self

        for component in self.components:
            found = component.find_child(name)
            if found is not None:
                return found

        return None


def main():
    # корінь карти
    city_map = MapGroup("Карта міста")

    # райони
    center = MapGroup("Центр", 10, 10)
    suburb = MapGroup("Передмістя", 50, 20)

    # об'єкти центру
    school = MapObject("Школа", 5, 3)
    hospital = MapObject("Лікарня", 8, 6)
    park = MapObject("Парк", 2, 4)

    # об'єкти передмістя
    shop = MapObject("Магазин", 4, 2)
    station = MapObject("Станція", 7, 5)

    # ще одна вкладена група
    residential = MapGroup("Житловий масив", 15, 10)
    house1 = MapObject("Будинок 1", 1, 1)
    house2 = MapObject("Будинок 2", 3, 2)

    residential.add_component(house1)
    residential.add_component(house2)

    center.add_component(school)
    center.add_component(hospital)
    center.add_component(park)

    suburb.add_component(shop)
    suburb.add_component(station)
    suburb.add_component(residential)

    city_map.add_component(center)
    city_map.add_component(suburb)

    # виведення карти
    print("=== Відображення карти міста ===")
    city_map.draw()

    # пошук елемента
    print("\n=== Пошук елемента ===")
    name_to_find = input("Введіть назву об'єкта: ")
    result = city_map.find_child(name_to_find)

    if result:
        print(f"Елемент '{result.name}' знайдено")
    else:
        print("Елемент не знайдено")


if __name__ == "__main__":
    main()