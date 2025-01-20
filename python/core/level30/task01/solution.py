from PIL import Image

# Открытие изображения
image_path = "path/to/your/image.jpg"  # Замените на путь к вашему изображению
image = Image.open(image_path)

# Извлечение размеров изображения


# Вывод размеров в консоль
print(image.size)

# Отображение изображения
image.show()