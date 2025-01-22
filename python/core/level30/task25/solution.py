from PIL import Image

# Создаем новое изображение размером 300x300 пикселей в формате RGBA
# Цвет фона (0, 0, 0, 0) означает полностью прозрачный
trans_image = Image.new('RGBA',(300,300),(0,0,0,0))

# Сохраняем изображение под именем "transparent_image.png"
trans_image.save("transparent_image.png")