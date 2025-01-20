from PIL import Image, ImageEnhance

# Загрузка изображения
input_image = "input.jpg"
image = Image.open(input_image)

# Изменение яркости
ench = ImageEnhance.Brightness(image)
b_img = ench.enhance(1.5)
b_img.save("output_brightness.jpg")

# Изменение контрастности
ench = ImageEnhance.Contrast(b_img)
h_img = ench.enhance(1.5)
h_img.save("output_contrast.jpg")

# Изменение насыщенности
ench = ImageEnhance.Color(h_img)
v_img = ench.enhance(0.5)
v_img.save("output_saturation.jpg")