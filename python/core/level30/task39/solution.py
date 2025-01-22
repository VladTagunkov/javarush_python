from PIL import Image
import os

# Путь к папке с изображениями
frames_folder = 'frames'

# Чтение всех изображений из указанной папки


# Конвертация изображений в GIF

    # Установка длительности кадра и бесконечного цикла
    
frames = []
for filename in os.listdir(frames_folder):
    img_path = os.path.join(frames_folder,filename)
    
    with Image.open(img_path) as img:
        conv_img = img.convert('GIF')
        frames.append(conv_img)
        
frames[0].save("animation.gif",save_all=True, append_images=frames[1:],
              duration=150,loop=0)