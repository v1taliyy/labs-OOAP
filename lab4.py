from abc import ABC, abstractmethod


# інтерфейс телефону
class Phone(ABC):
    @abstractmethod
    def make_call(self):
        pass


# звичайний Skype
class SkypePhone(Phone):
    def make_call(self):
        print("Здійснюється звичайний дзвінок у Skype")


# окремий клас камери
class VideoCamera:
    def start_video(self):
        print("Відеокамера увімкнена")


# Adapter
# робить VideoCamera сумісною з інтерфейсом Phone
class VideoCallAdapter(Phone):
    def __init__(self, camera):
        self.camera = camera

    def make_call(self):
        self.camera.start_video()
        print("Здійснюється відеодзвінок у Skype")


def main():
    print("1 - Звичайний дзвінок")
    print("2 - Відеодзвінок")

    choice = input("Ваш вибір: ")

    if choice == "1":
        phone = SkypePhone()
    elif choice == "2":
        camera = VideoCamera()
        phone = VideoCallAdapter(camera)
    else:
        print("Невірний вибір")
        return

    phone.make_call()


if __name__ == "__main__":
    main()