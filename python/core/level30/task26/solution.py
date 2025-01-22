from PIL import Image

# Открываем изображение
image = Image.open("image.png")

# Преобразуем изображение в режим RGBA
rgba_image = image.convert("RGBA")

# Получаем данные пикселей изображения
width,height = image.size

# Устанавливаем альфа-значение 100 для каждого пикселя
for x in range(width):
    for y in range(height):
        r,g,b,a = rgba_image.getpixel((x,y))
        rgba_image.putpixel((x,y),(r,g,b,100))

    # Изменяем альфа-канал (четвертый элемент кортежа)


# Обновляем изображение с новыми данными


# Сохраняем измененное изображение
rgba_image.save("semi_transparent_image.png")