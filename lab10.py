from abc import ABC, abstractmethod


# стратегія друку
class PrintStrategy(ABC):
    @abstractmethod
    def print_document(self, size, color, pages):
        pass


# лазерний принтер
class LaserPrinter(PrintStrategy):
    def print_document(self, size, color, pages):
        print("\n=== Лазерний принтер ===")
        print(f"Формат: {size}")
        print(f"Колірність: {color}")
        print(f"Кількість сторінок: {pages}")
        print("Документ надруковано на лазерному принтері.")


# кольоровий принтер
class ColorPrinter(PrintStrategy):
    def print_document(self, size, color, pages):
        print("\n=== Кольоровий принтер ===")
        print(f"Формат: {size}")
        print(f"Колірність: {color}")
        print(f"Кількість сторінок: {pages}")
        print("Документ надруковано на кольоровому принтері.")


# плотер
class PlotterPrinter(PrintStrategy):
    def print_document(self, size, color, pages):
        print("\n=== Плотер ===")
        print(f"Формат: {size}")
        print(f"Колірність: {color}")
        print(f"Кількість сторінок: {pages}")
        print("Документ надруковано на плотері.")


# клас для вибору стратегії
class PrinterContext:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute_print(self, size, color, pages):
        if self.strategy is None:
            print("Принтер не вибрано.")
        else:
            self.strategy.print_document(size, color, pages)


# підбір оптимального принтера
def choose_printer(size, color, pages):
    # якщо великий формат - плотер
    if size in ["A2", "A1", "A0"]:
        return PlotterPrinter()

    # якщо потрібен кольоровий друк
    if color.lower() == "кольоровий":
        return ColorPrinter()

    # якщо ч/б і багато сторінок - лазерний
    if color.lower() == "чорно-білий" and pages >= 10:
        return LaserPrinter()

    # за замовчуванням
    return LaserPrinter()


def main():
    print("=== Система друку ===")

    size = input("Введіть формат (A4, A3, A2, A1, A0): ")
    color = input("Введіть колірність (кольоровий / чорно-білий): ")
    pages = int(input("Введіть кількість сторінок: "))

    context = PrinterContext()

    # вибір стратегії
    printer = choose_printer(size, color, pages)
    context.set_strategy(printer)

    # друк
    context.execute_print(size, color, pages)


if __name__ == "__main__":
    main()