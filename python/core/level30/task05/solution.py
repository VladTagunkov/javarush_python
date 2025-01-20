from PIL import Image

# Загрузка изображения из файла
original_image = Image.open("input_image.jpg")

# Изменение размера изображения до 800x600 пикселей
image = original_image.resize((800,600))

# Сохранение измененного изображения в новый файл
image.save("resized_image.jpg")