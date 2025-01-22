from PIL import Image
import os

# Путь к исходному и сжатому изображениям
input_image_path = 'input_image.jpg'
output_image_path = 'compressed_image.jpg'

# Открытие изображения с использованием Pillow
image = Image.open(input_image_path)
image.save(output_image_path,quality=50)
# Сохранение изображения с качеством 50 для сжатия


# Получение размеров файлов
input_size = os.path.getsize(input_image_path)
output_size = os.path.getsize(output_image_path)

# Вывод размеров файлов
print(f"Размер файла '{input_image_path}': {input_size} байт")
print(f"Размер файла '{output_image_path}': {output_size} байт")
