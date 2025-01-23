from moviepy.editor import VideoFileClip
from PIL import Image
import os

# Путь к видеофайлу и выходной папке для кадров
video_path = 'example_video.mp4'
output_folder = 'output_frames'

# Проверяем наличие выходной папки и создаем ее, если она не существует
os.makedirs(output_folder, exist_ok=True)

# Загрузка видео с использованием MoviePy
video = VideoFileClip(video_path)
duration = int(video.duration)

# Извлечение и обработка каждого кадра по секундам
for i in range(duration):
    # Извлечение кадра в текущую секунду
    frame = video.get_frame(i)

    # Преобразование кадра (numpy array) в изображение PIL
    img = Image.fromarray(frame)

    # Изменение размера изображения до 100x100 пикселей
    img_res = img.resize((100,100))

    # Сохранение изображения в указанной выходной папке
    img_res.save(f"{output_folder}/frame_{i}.png")

