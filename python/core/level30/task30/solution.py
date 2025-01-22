from PIL import Image

# Открываем изображение с именем 'input_image.jpg'
input_image_path = 'input_image.jpg'
output_image_path = 'output_image.png'

# Используем библиотеку Pillow для открытия изображения
image = Image.open(input_image_path)
    # Конвертируем изображение в формат PNG
image.save(output_image_path)

