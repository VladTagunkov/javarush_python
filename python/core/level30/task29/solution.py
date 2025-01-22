from PIL import Image

# Открытие изображения
image = Image.open("input_image.jpg")

# Вывод формата изображения
print(image.format)