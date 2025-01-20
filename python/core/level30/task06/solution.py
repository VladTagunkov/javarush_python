from PIL import Image

# Путь к исходному и результирующему изображениям
input_image_path = "input.jpg"  # Замените это имя файла на актуальный путь вашего изображения
output_image_path = "thumbnail_image.jpg"

# Максимальный размер миниатюры
max_size = (400,400)

# Открываем изображение
with Image.open(input_image_path) as img:
    # Уменьшаем изображение, сохраняя пропорции
    img.thumbnail((400,400))
    # Сохраняем уменьшенное изображение
    img.save(output_image_path)

print(f"Миниатюра сохранена в '{output_image_path}' с максимальным размером {max_size}.")
