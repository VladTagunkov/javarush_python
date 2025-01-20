from PIL import Image

# Открываем исходное изображение
input_image_path = "input_image.jpg"  # замените на путь к вашему изображению
image = Image.open(input_image_path)

# Поворот изображения на 90 градусов против часовой стрелки
rot_img = image.rotate(90)
rot_img.save("rotated_90.jpg")

# Поворот изображения на 45 градусов с параметром expand=True
ang_img = rot_img.rotate(45,expand=True)
ang_img.save("rotated_expanded_45.jpg")