# базовий клас
class Employee:
    def __init__(self, name):
        self.name = name

    def get_income(self):
        return 0

    def __str__(self):
        return f"{self.name} | Дохід: {self.get_income()}"


# самозайнятий
class SelfEmployed(Employee):
    def __init__(self, name, income):
        super().__init__(name)
        self.income = income

    def get_income(self):
        return self.income


# з постійним окладом
class SalariedEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def get_income(self):
        return self.salary


# безробітний
class Unemployed(Employee):
    def __init__(self, name, benefit):
        super().__init__(name)
        self.benefit = benefit

    def get_income(self):
        return self.benefit


# колекція працівників
class EmployeeCollection:
    def __init__(self):
        self.employees = []

    def add(self, employee):
        self.employees.append(employee)

    def __iter__(self):
        return EmployeeIterator(self.employees)


# ітератор
class EmployeeIterator:
    def __init__(self, employees):
        # сортуємо по 2 ознаках:
        # 1) дохід
        # 2) ім'я
        self.sorted = sorted(employees, key=lambda e: (e.get_income(), e.name))
        self.index = 0

    def __next__(self):
        if self.index < len(self.sorted):
            result = self.sorted[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __iter__(self):
        return self


def main():
    collection = EmployeeCollection()

    # додаємо різних працівників
    collection.add(SelfEmployed("Іван", 7000))
    collection.add(SalariedEmployee("Олена", 10000))
    collection.add(Unemployed("Петро", 2000))
    collection.add(SelfEmployed("Андрій", 5000))
    collection.add(SalariedEmployee("Марія", 8000))

    print("=== Список працівників (відсортований) ===")

    # перебір через ітератор
    for emp in collection:
        print(emp)


if __name__ == "__main__":
    main()