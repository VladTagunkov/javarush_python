import os
from moviepy.editor import VideoFileClip
from PIL import Image
import numpy as np

# Путь к видеофайлу и выходной директории
video_path = "your_video.mp4"  # Укажите путь к вашему видеофайлу
output_dir = "output_frames"

# Интервал кадров
frame_interval = 5

# Создаем директорию output_frames, если она не существует
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Загрузка видеофайла
video = VideoFileClip(video_path)

# Количество кадров в видео
frame_interval = 5

# Извлечение каждого пятого кадра
for i,frame in enumerate(video.iter_frames()):
    if i % frame_interval == 0:
        img = Image.fromarray(frame)
        img_b = img.convert("L")
        img_b.save(f"{output_dir}/frame_b_{i}.png")

    # Получение кадра


    # Преобразование кадра в черно-белое изображение


    # Сохранение изображения


# Закрытие клипа для освобождения ресурсов
clip.close()
