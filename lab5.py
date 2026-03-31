# Базовий клас зображення
class Image:
    def get_name(self):
        pass

    def get_type(self):
        pass

    def get_pixels(self):
        pass

    def get_size(self):
        pass

    def get_filters(self):
        return []


# Конкретне зображення
class BasicImage(Image):
    def __init__(self, name, image_type, pixels, size):
        self.name = name
        self.image_type = image_type
        self.pixels = pixels
        self.size = size

    def get_name(self):
        return self.name

    def get_type(self):
        return self.image_type

    def get_pixels(self):
        return self.pixels

    def get_size(self):
        return self.size

    def get_filters(self):
        return []


# Базовий декоратор
class ImageDecorator(Image):
    def __init__(self, image):
        self.image = image

    def get_name(self):
        return self.image.get_name()

    def get_type(self):
        return self.image.get_type()

    def get_pixels(self):
        return self.image.get_pixels()

    def get_size(self):
        return self.image.get_size()

    def get_filters(self):
        return self.image.get_filters()


# Фільтр розмитість
class BlurFilter(ImageDecorator):
    def get_size(self):
        return self.image.get_size() + 2.5

    def get_filters(self):
        return self.image.get_filters() + ["Розмитість"]


# Фільтр чіткість
class SharpnessFilter(ImageDecorator):
    def get_size(self):
        return self.image.get_size() + 1.5

    def get_filters(self):
        return self.image.get_filters() + ["Чіткість"]


# Фільтр насиченість
class SaturationFilter(ImageDecorator):
    def get_size(self):
        return self.image.get_size() + 1.0

    def get_filters(self):
        return self.image.get_filters() + ["Насиченість"]


# Фільтр художній шум
class ArtisticNoiseFilter(ImageDecorator):
    def get_size(self):
        return self.image.get_size() + 3.0

    def get_filters(self):
        return self.image.get_filters() + ["Художній шум"]


# Вирізання у формі кола
class CircleCropFilter(ImageDecorator):
    def get_size(self):
        return self.image.get_size() - 2.0

    def get_filters(self):
        return self.image.get_filters() + ["Вирізання колом"]


# Вирізання у формі прямокутника
class RectangleCropFilter(ImageDecorator):
    def get_size(self):
        return self.image.get_size() - 1.5

    def get_filters(self):
        return self.image.get_filters() + ["Вирізання прямокутником"]


# Фасад для роботи з колекцією зображень
class ImageManager:
    def __init__(self):
        self.images = []

    # додаємо зображення в список
    def add_image(self, image):
        self.images.append(image)

    # показати всі зображення
    def show_all_images(self):
        print("\n=== Список зображень ===")
        for image in self.images:
            print(f"Назва: {image.get_name()} | Розмір: {image.get_size():.2f} МБ")

    # відбір по фільтру
    def filter_by_effect(self, filter_name):
        print(f"\n=== Зображення з фільтром: {filter_name} ===")
        found = False
        for image in self.images:
            if filter_name in image.get_filters():
                print(f"Назва: {image.get_name()} | Розмір: {image.get_size():.2f} МБ")
                found = True
        if not found:
            print("Нічого не знайдено")

    # сортування за розміром
    def sort_by_size(self):
        self.images.sort(key=lambda image: image.get_size())
        print("\n=== Відсортовано за розміром ===")
        for image in self.images:
            print(f"Назва: {image.get_name()} | Розмір: {image.get_size():.2f} МБ")


def main():
    manager = ImageManager()

    # створюємо базові зображення
    img1 = BasicImage("Фото1", "Кольорове", 500000, 10.0)
    img2 = BasicImage("Фото2", "Чорно-біле", 300000, 7.5)
    img3 = BasicImage("Фото3", "Кольорове", 800000, 15.0)

    # застосовуємо декоратори (фільтри)
    img1 = BlurFilter(SaturationFilter(img1))
    img2 = SharpnessFilter(CircleCropFilter(img2))
    img3 = ArtisticNoiseFilter(RectangleCropFilter(img3))

    # додаємо в список
    manager.add_image(img1)
    manager.add_image(img2)
    manager.add_image(img3)

    # показуємо всі
    manager.show_all_images()

    # відбір по фільтру
    manager.filter_by_effect("Розмитість")
    manager.filter_by_effect("Вирізання колом")

    # сортування
    manager.sort_by_size()


if __name__ == "__main__":
    main()