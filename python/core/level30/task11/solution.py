from PIL import Image

# Открываем исходное изображение
input_image_path = 'input.jpg'
image = Image.open(input_image_path)

# Переворачиваем изображение по горизонтали
trans_h = image.transpose(Image.FLIP_LEFT_RIGHT)
trans_h.save("flipped_horizontal.jpg")

# Переворачиваем изображение по вертикали
trans_v = image.transpose(Image.FLIP_TOP_BOTTOM)
trans_v.save("flipped_vertical.jpg")