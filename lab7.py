from abc import ABC, abstractmethod


# базовий обробник
class TransferHandler(ABC):
    def __init__(self):
        self.next_handler = None

    # зв'язуємо ланцюжок
    def set_next(self, handler):
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle(self, amount, receiver):
        pass


# банківський переказ
class BankTransferHandler(TransferHandler):
    def handle(self, amount, receiver):
        if amount > 5000:
            print(f"Переказ {amount} грн для {receiver} виконано через банківський переказ")
        elif self.next_handler:
            self.next_handler.handle(amount, receiver)
        else:
            print("Немає доступного способу переказу")


# WesternUnion
class WesternUnionHandler(TransferHandler):
    def handle(self, amount, receiver):
        if 2000 < amount <= 5000:
            print(f"Переказ {amount} грн для {receiver} виконано через WesternUnion")
        elif self.next_handler:
            self.next_handler.handle(amount, receiver)
        else:
            print("Немає доступного способу переказу")


# Unistream
class UnistreamHandler(TransferHandler):
    def handle(self, amount, receiver):
        if 1000 < amount <= 2000:
            print(f"Переказ {amount} грн для {receiver} виконано через Unistream")
        elif self.next_handler:
            self.next_handler.handle(amount, receiver)
        else:
            print("Немає доступного способу переказу")


# PayPal
class PayPalHandler(TransferHandler):
    def handle(self, amount, receiver):
        if 0 < amount <= 1000:
            print(f"Переказ {amount} грн для {receiver} виконано через PayPal")
        elif self.next_handler:
            self.next_handler.handle(amount, receiver)
        else:
            print("Немає доступного способу переказу")


def main():
    # створюємо обробники
    bank = BankTransferHandler()
    western = WesternUnionHandler()
    unistream = UnistreamHandler()
    paypal = PayPalHandler()

    # формуємо ланцюжок
    paypal.set_next(unistream).set_next(western).set_next(bank)

    print("=== Система переказу коштів ===")
    receiver = input("Введіть ім'я отримувача: ")
    amount = float(input("Введіть суму переказу: "))

    # запуск ланцюжка
    paypal.handle(amount, receiver)


if __name__ == "__main__":
    main()