from moviepy.editor import VideoFileClip
import numpy as np

# Путь к входному и выходному видеофайлам
input_video_path = "input_video.mp4"  # Укажите путь к вашему видео файлу
output_video_path = "brightened_video.mp4"

# Функция для увеличения яркости изображения
def increase_brightness(image):
    # Увеличение яркости на 20%
    return image * 1.2

# Загрузка видео
clip = VideoFileClip(input_video_path)

# Применение изменения яркости ко всем кадрам видео
brightened_clip = clip.fl_image(lamda frame: increase_brightness(frame))

# Сохранение результата в новый файл
brightened_clip.write_videofile(output_video_path, codec='libx264')

