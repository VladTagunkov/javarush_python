from PIL import Image, ImageFilter

# Открытие изображения
input_image = Image.open("input.jpg")

# Применение фильтра размытия (BLUR)
b_img = input_image.filter(ImageFilter.BLUR)
b_img.save("output_blur.jpg")

# Применение фильтра контуры (CONTOUR)
c_img = input_image.filter(ImageFilter.CONTOUR)
c_img.save("output_contour.jpg")

# Применение фильтра усиление резкости (SHARPEN)
s_img = input_image.filter(ImageFilter.SHARPEN)
s_img.save("output_sharpen.jpg")