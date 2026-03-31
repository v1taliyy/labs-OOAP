# спостерігач
class Client:
    def __init__(self, name, bet):
        self.name = name
        self.bet = bet

    # отримати оновлення від матчу
    def update(self, minute, score):
        print(f"[{self.name}] Хвилина: {minute}, рахунок: {score}, моя ставка: {self.bet}")

        # приклад зміни ставки під час матчу
        if minute == 30 and self.name == "Клієнт 1":
            self.bet = "Перемога Карпат"
            print(f"{self.name} змінив ставку на: {self.bet}")

        if minute == 60 and self.name == "Клієнт 2":
            self.bet = "Нічия"
            print(f"{self.name} змінив ставку на: {self.bet}")


# суб’єкт
class FootballMatch:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.observers = []
        self.score = "0:0"

    # підписка
    def attach(self, observer):
        self.observers.append(observer)

    # відписка
    def detach(self, observer):
        self.observers.remove(observer)

    # сповіщення всіх клієнтів
    def notify(self, minute):
        for observer in self.observers:
            observer.update(minute, self.score)

    # зміна рахунку
    def set_score(self, score):
        self.score = score

    # моделювання матчу
    def play_match(self):
        print(f"Матч: {self.team1} - {self.team2}")
        print("Матч розпочався\n")

        for minute in [15, 30, 45, 60, 75, 90]:
            if minute == 45:
                self.set_score("1:0")
            elif minute == 75:
                self.set_score("1:1")
            elif minute == 90:
                self.set_score("2:1")

            print(f"\n--- {minute} хвилина ---")
            self.notify(minute)

        print("\nМатч завершено")
        print(f"Фінальний рахунок: {self.score}")


def main():
    # створюємо матч
    match = FootballMatch("Карпати", "Динамо")

    # створюємо клієнтів
    client1 = Client("Клієнт 1", "Перемога Динамо")
    client2 = Client("Клієнт 2", "Тотал більше 2.5")

    # підписуємо клієнтів на матч
    match.attach(client1)
    match.attach(client2)

    # запуск матчу
    match.play_match()


if __name__ == "__main__":
    main()