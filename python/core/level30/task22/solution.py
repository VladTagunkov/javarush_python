from PIL import Image, ImageDraw, ImageFont

# Функция для добавления водяного знака на изображение
def add_watermark(input_image_path, output_image_path, watermark_text):
    # Открываем исходное изображение и переводим его в режим RGBA для прозрачности
    image = Image.open(input_image_path).convert("RGBA")

    # Создаем новый слой с прозрачностью для текста
    trans = Image.new("RGBA",(image.size[0],image.size[1]),(255,255,255,0))

    # Выбираем шрифт и размер (по умолчанию используем системный шрифт)
    font = ImageFont.truetype('arial.ttf',14)

    # Инициализируем объект для рисования на слое с текстом
    draw = ImageDraw.Draw(trans)

    # Рассчитываем размер текста и его позицию для размещения в правом нижнем углу
    width,height = image.size
    text_width,text_height = draw.textsize(watermark_text,font=font)
    x = width - text_width - 10
    y = height - text_height - 10
    
    # Добавляем текст с прозрачностью
    draw.text((x,y),watermark_text,font=font,fill=(255,255,255,128))

    # Объединяем исходное изображение и слой с текстом
    image = Image.alpha_composite(image,trans)

    # Переводим изображение обратно в режим RGB и сохраняем как JPEG
    image.convert('RGB').save(output_image_path)

# Пример использования
add_watermark("input_image.jpg", "watermarked_image.jpg", "© 2023 Student Name")
