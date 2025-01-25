from moviepy.editor import VideoFileClip
import numpy as np
from moviepy.video.fx.all import colorx

# Путь к входному и выходному видеофайлам
input_video = "input_video.mp4"  # Укажите путь к вашему видеофайлу
output_video = "sepia_video.mp4"

# Функция для применения фильтра сепии к кадру изображения
def apply_sepia(image):
    sepia_matrix = np.array([[0.393, 0.769, 0.189],
                             [0.349, 0.686, 0.168],
                             [0.272, 0.534, 0.131]])
    sepia_img = image.dot(sepia_matrix.T)                         
    #sepia_filter = np.clip(sepia_img, 0, 255)
    sepia_image = np.clip(sepia_img, 0, 255)
    sepia_image[sepia_image > 255] = 255  # Ограничение значений пикселей
    return sepia_image.astype(np.uint8)

# Загрузка исходного видео
video_clip = VideoFileClip(input_video)

# Применение фильтра сепии ко всем кадрам видео
sepia_clip = video_clip.fl_image(apply_sepia)

# Сохранение отредактированного видео в файл
sepia_clip.write_videofile(output_video, codec='libx264')