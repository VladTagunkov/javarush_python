from PIL import Image, ImageDraw

def add_text_to_image(input_image_path, output_image_path, text):
    # Открываем изображение
    image = Image.open(input_image_path)
    width,height = image.size

    # Создаем объект для рисования
    draw = ImageDraw.Draw(image)

    # Определяем позицию для текста

    # Цвет текста (белый)
    draw.text((0,0),text,fill="white")

    # Добавляем текст на изображение
    draw.text()

    # Сохраняем изображение с добавленным текстом
    image.save(output_image_path)

# Параметры
input_image_path = 'input_image.jpg'
output_image_path = 'output_image.jpg'
text = 'Hello World!'

# Вызов функции для добавления текста
add_text_to_image(input_image_path, output_image_path, text)