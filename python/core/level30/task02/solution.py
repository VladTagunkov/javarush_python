from PIL import Image

# Путь к входному и выходному изображениям
input_path = 'input.jpg'  # Укажите путь к вашему изображению
output_path = 'output.jpg'  # Укажите путь для сохраненного изображения

# Заданный размер для изменения
size = (200,200)

# Открытие файла изображения
with Image.open(input_path) as img:
    # Изменение размера изображения
    resized_img = img.resize(size)
    # Сохранение измененного изображения под новым именем
    resized_img.save(output_path)

    # Проверка нового размера
    if resized_img.size != size:
        raise ValueError(f"Изображение не было изменено корректно, текущий размер: {resized_img.size}")

print(f"Изображение сохранено в '{output_path}' с размером {size}.")
