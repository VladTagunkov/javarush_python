from PIL import Image

# Параметры для обрезки
input_image_path = 'input.jpg'  # Путь к исходному изображению
output_image_path = 'basic_cropped.jpg'  # Путь для сохранения обрезанного изображения
crop_width = 200
crop_height = 200

# Открытие исходного изображения
image = Image.open(input_image_path)

# Получение размеров исходного изображения
size = image.size

# Вычисление координат для центральной обрезки
left = (size[0] - crop_width)/2
top = (size[1] - crop_height)/2
right = (size[0] + crop_width)/2
bottom = (size[1] + crop_height)/2
# Выполнение обрезки
cut_img = image.crop((left,top,right,bottom))

# Сохранение обрезанного изображения
cut_img.save(output_image_path)

