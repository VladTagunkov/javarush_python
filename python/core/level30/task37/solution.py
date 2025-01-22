import os
from PIL import Image

# Указание директорий для входных и выходных данных
input_dir = 'input_images'
output_dir = 'output_images'

# Создаем директорию для выходных изображений, если она не существует
os.makedirs(output_dir, exists_ok=True)

# Установленные размеры
new_size = (640,640)


# Проход по каждому файлу в папке input_images
for filename in os.listdir(input_dir):
    # Проверка на нужные расширения
    if filename.endswith(('.jpg','.jpeg','.png'))
        # Открываем изображение
        img_path = os.path.join(input_dir,filename)
        
        with Image.open(img_path) as img:
            img.thumbnail(new_size)
            # Изменяем размер изображения с сохранением пропорций
            out_path = os.path.join(output_dir,filename)
            # Получаем путь для сохранения обработанного изображения
            
            # Сохраняем изображение 
            img.save(out_path)