from moviepy.editor import VideoFileClip
from moviepy.video.fx.all import colorx, blackwhite, lum_contrast, blackwhite
import numpy as np

# Путь к входному и выходному видеофайлам
input_video_path = "input_video.mp4"  # Укажите путь к вашему видео файлу
output_video_path = "high_contrast_bw_video.mp4"

# Коэффициент увеличения контрастности
contrast_factor = 1.5

# Загрузка видео
video = VideoFileClip(input_video_path)

# Увеличение контрастности на 50%
h_video = lum_contrast(video, contrast=contrast_factor)

# Преобразование в черно-белый формат
bh_cid = blackwhite(h_video)

# Сохранение результата в новый файл
bh_cid.write_videofile(output_video_path)
