from PIL import Image

# Загрузка изображения
image = Image.open("input.jpg")

# Преобразование в черно-белый режим (L)
img_l = image.convert('L')
img_l.save("output_gray.jpg")

# Преобразование в режим CMYK
img_c = image.convert('CMYK')
img_c.save("output_cmyk.jpg")

# Преобразование в режим RGBA
img_r = image.convert('RGBA')
img_r.save("output_rgba.png")
