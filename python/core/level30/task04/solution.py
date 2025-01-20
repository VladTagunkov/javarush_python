import os
from PIL import Image, ImageEnhance

# Указание директорий для входных и выходных изображений
input_dir = "path_to_input_directory"  # Укажите путь к вашей директории с изображениями
output_dir = "path_to_output_directory"  # Укажите путь для сохранения обработанных изображений

# Создание выходной директории, если она не существует
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Обработка всех файлов в входной директории
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
        # Полный путь к входному и выходному файлу
        input_file_path = os.path.join(input_dir, filename)
        output_file_path = os.path.join(output_dir, filename)

        # Открытие файла изображения
        with Image.open(input_file_path) as img:
            # Изменение размера изображения до 300x300
            img = img.resize((???), Image.ANTIALIAS)

            # Поворот изображения на 45 градусов
            img = img.rotate(???, expand=True)

            # Повышение яркости на 1.5
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(???)

            # Сохранение модифицированного изображения в выходной директории
            img.save(output_file_path)

print("Обработка изображений завершена.")
