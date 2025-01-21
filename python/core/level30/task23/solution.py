from PIL import Image, ImageDraw

# Загрузка изображения
input_image_path = "input_image.jpg"
output_image_path = "graphics_image.jpg"
image = Image.open(input_image_path)
draw = ImageDraw.Draw(image)

width,height = image.size
# Рисование красной линии
draw.line((0,0,width,height),fill='red',width=2)

# Рисование синего прямоугольника
draw.rectangle((100,100,200,200),outline='blue',width=2)

# Рисование зеленого круга
draw.ellipse((100,100,200,200), outline='green', width=4)

# Сохранение измененного изображения
image.save(output_image_path)