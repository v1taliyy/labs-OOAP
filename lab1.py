from dataclasses import dataclass, field, replace
from typing import Tuple, Dict, Optional


# Клас користувача.
# frozen=True означає, що після створення об'єкт змінювати не можна.
@dataclass(frozen=True)
class User:
    full_name: str
    department: str


# Клас автомобіля.
@dataclass(frozen=True)
class Car:
    plate_number: str
    brand: str
    model: str
    current_user: Optional[User] = None
    previous_users: Tuple[User, ...] = field(default_factory=tuple)

    # Метод зміни користувача.
    def change_user(self, new_user: User) -> "Car":

        if self.current_user is None:
            return replace(self, current_user=new_user)

        updated_history = self.previous_users + (self.current_user,)

        # Повертаємо новий об'єкт Car з новим користувачем.
        return replace(self, current_user=new_user, previous_users=updated_history)


# Клас журналу реєстрації автомобілів.
class CarRegistry:
    def __init__(self):
        # Ключ словника — номер авто, значення — об'єкт Car.
        self._cars: Dict[str, Car] = {}

    # Додавання автомобіля в журнал.
    def add_car(self, car: Car):
        if car.plate_number in self._cars:
            print(f"Автомобіль з номером {car.plate_number} вже є в системі.")
        else:
            self._cars[car.plate_number] = car
            print(f"Автомобіль {car.brand} {car.model} успішно додано.")

    # Призначення або зміна користувача для авто.
    def assign_user(self, plate_number: str, user: User):
        if plate_number not in self._cars:
            print(f"Автомобіль з номером {plate_number} не знайдено.")
            return

        old_car = self._cars[plate_number]
        new_car = old_car.change_user(user)

        # Оновлюємо запис у журналі.
        self._cars[plate_number] = new_car
        print(f"Для авто {plate_number} призначено користувача: {user.full_name}")

    # Виведення інформації про одне авто.
    def show_car_info(self, plate_number: str):
        car = self._cars.get(plate_number)

        if not car:
            print("Авто не знайдено.")
            return

        print("\n=== Інформація про автомобіль ===")
        print(f"Марка: {car.brand} {car.model}")
        print(f"Номер: {car.plate_number}")

        if car.current_user:
            print(f"Поточний користувач: {car.current_user.full_name} ({car.current_user.department})")
        else:
            print("Поточний користувач: відсутній")

        if car.previous_users:
            print("Історія користувачів:")
            for i, user in enumerate(car.previous_users, start=1):
                print(f"{i}) {user.full_name} ({user.department})")
        else:
            print("Історія користувачів: відсутня")

    # Виведення всіх автомобілів у журналі.
    def show_all_cars(self):
        if not self._cars:
            print("Журнал порожній.")
            return

        print("\n=== Журнал автомобілів ===")
        for car in self._cars.values():
            current = car.current_user.full_name if car.current_user else "Немає користувача"
            print(f"Номер: {car.plate_number} | Авто: {car.brand} {car.model} | Користувач: {current}")


# Головна частина програми.
def main():
    registry = CarRegistry()

    # Створюємо кількох користувачів.
    user1 = User("Микола Попович", "Бухгалтерія")
    user2 = User("Віталій Коваль", "Відділ кадрів")
    user3 = User("Андрій Яремчук", "IT-відділ")

    # Створюємо автомобілі.
    car1 = Car("AA1234BB", "Toyota", "Corolla")
    car2 = Car("BC5678CD", "Skoda", "Octavia")

    # Додаємо авто в журнал.
    registry.add_car(car1)
    registry.add_car(car2)

    print()

    # Призначаємо користувачів.
    registry.assign_user("AA1234BB", user1)
    registry.assign_user("AA1234BB", user2)
    registry.assign_user("AA1234BB", user3)

    registry.assign_user("BC5678CD", user2)

    # Показуємо увесь журнал.
    registry.show_all_cars()

    # Показуємо детальну інформацію по конкретному авто.
    registry.show_car_info("AA1234BB")


if __name__ == "__main__":
    main()