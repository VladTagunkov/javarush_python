import os
from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_folder, output_folder, watermark_text, font_path, font_size):
    # Создаем выходную папку, если она не существует
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Проходим по всем файлам в папке с изображениями
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif', 'tiff')):
            # Открываем изображение
            img_path = os.path.join(input_folder,filename)
            with Image.open(img_path) as img:
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype('arial.ttf',30)
                width, height = img.size
                
                text_width,text_height = draw.textsize(watermark_text,font=font)
                x = width - text_width-10
                y = height - text_height - 10
                
                draw.text((x,y), watermark_text, font=font, fill=(255,255,255,128))
                out_path = os.path.join(output_folder,filename)
                img.save(out_path)
                
            # Создаем объект для рисования

            
            # Загружаем шрифт

            
            # Размер текста

            
            # Позиция текста в правом нижнем углу

            
            # Добавляем водяной знак

            
            # Сохраняем изображение


# Параметры
input_folder = 'images'
output_folder = 'watermarked_images'
watermark_text = 'Sample Watermark'
font_path = 'arial.ttf'  # путь к файлу шрифта Arial
font_size = 30

add_watermark(input_folder, output_folder, watermark_text, font_path, font_size)