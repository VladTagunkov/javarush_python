from PIL import Image
import os

# Задаем пути к входному и выходному изображениям
input_path = 'input.jpg'  # Укажите путь к вашему изображению
output_path = 'output.png'  # Укажите путь для сохранения нового изображения

# Открываем изображение
with Image.open(input_path) as img:
    # Получаем EXIF-данные
    exif_data = img._getexif()
    if exif_data is not None:
        exif_bytes = img.info['exif']
    else:
        print("EXIF data is not presented.")
    
    if exif_data is not None:
    # Конвертация в другой формат и сохранение с оптимизацией и EXIF-данными
        img.save(output_path,format='PNG',exif=exif_bytes,optimize=True)
    else:
        img.save(output_path,format='PNG',optimize=True)

print(f"Изображение было успешно преобразовано и сохранено в {output_path}.")
