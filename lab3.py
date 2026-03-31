from copy import deepcopy
import os


# мешканець
class Resident:
    def __init__(self, full_name, birth_date, group):
        self.full_name = full_name
        self.birth_date = birth_date
        self.group = group

    def __str__(self):
        return (
            f"ПІБ: {self.full_name}\n"
            f"Дата народження: {self.birth_date}\n"
            f"Група: {self.group}"
        )


# кімната
class Room:
    def __init__(self, room_number, total_payment):
        self.room_number = room_number
        self.total_payment = total_payment
        self.residents = []

    # Prototype — копіюємо кімнату
    def clone(self):
        return deepcopy(self)

    # додаємо мешканця
    def add_resident(self, resident):
        if len(self.residents) < 4:
            self.residents.append(resident)
        else:
            print("Максимум 4 мешканці!")

    # оплата на одного
    def payment_per_resident(self):
        if len(self.residents) == 0:
            return 0
        return self.total_payment / len(self.residents)

    # текст звіту
    def get_report(self):
        report = []
        report.append(f"Кімната № {self.room_number}")
        report.append(f"Кількість мешканців: {len(self.residents)}")
        report.append(f"Квартплата на 1: {self.payment_per_resident():.2f} грн")

        for i, r in enumerate(self.residents, 1):
            report.append(f"\nМешканець {i}:")
            report.append(str(r))

        return "\n".join(report)


# гуртожиток
class Dormitory:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    # запис у файл
    def generate_report_file(self, filename):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                for room in self.rooms:
                    f.write(room.get_report())
                    f.write("\n" + "=" * 40 + "\n")

            print(f"\nЗвіт створено: {os.path.abspath(filename)}")
        except Exception as e:
            print("Помилка при створенні файлу:", e)


def main():
    dormitory = Dormitory()

    # шаблон кімнати
    template = Room(0, 4000)

    n = int(input("Скільки кімнат? "))

    for i in range(n):
        print(f"\n--- Кімната {i + 1} ---")

        room = template.clone()
        room.room_number = input("Номер кімнати: ")

        count = int(input("Скільки мешканців (макс 4): "))
        count = min(count, 4)

        for j in range(count):
            print(f"\nМешканець {j + 1}:")
            name = input("ПІБ: ")
            birth = input("Дата народження: ")
            group = input("Група: ")

            room.add_resident(Resident(name, birth, group))

        dormitory.add_room(room)

    dormitory.generate_report_file("zvit.txt")


if __name__ == "__main__":
    main()