from PIL import Image

# Загрузка двух изображений
image1 = Image.open('image1.jpg')
image2 = Image.open('image2.jpg')

# Проверка, что изображения одинакового размера
if image1.size==image2.size:
    print(True)
else:
    print(False)

# Наложение одного изображения поверх другого
image1.paste(image2)

# Сохранение итогового изображения
image1.save("combined_image.jpg")