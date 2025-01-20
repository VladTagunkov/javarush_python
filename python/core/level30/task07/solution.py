from PIL import Image, ImageOps

# Путь к исходному и результирующему изображениям
input_image_path = 'input.jpg'  # Укажите актуальный путь к вашему изображению
output_image_path = 'fitted_image.jpg'

# Заданный размер для изменения и обрезки
size = (300,300)

# Открываем изображение
with Image.open(input_image_path) as image:
    # Изменение размера и обрезка с использованием ImageOps.fit
    fitted_image = ImageOps.fit(image,size,method=Image.LANCZOS)
    # Сохранение результата по указанному пути
    fitted_image.save(output_image_path)

print(f"Изображение сохранено в '{output_image_path}' с размером {size}.")
