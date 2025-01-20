from PIL import Image, ImageEnhance

# Открытие изображения
image_path = 'input_image.jpg'  # Замените на путь к вашему изображению
image = Image.open(image_path)

# Поворот изображения на 90 градусов против часовой стрелки
rotated_image = image.rotate(-90)

# Изменение яркости изображения (уменьшение вдвое)
enhancer = ImageEnhance.Brightness(rotated_image)
darker_image = enhancer.enhance(0.5)

# Сохранение обработанного изображения
output_image_path = 'output_image.jpg'
darker_image.save(output_image_path)

# Отображение обработанного изображения на экране
darker_image.show()