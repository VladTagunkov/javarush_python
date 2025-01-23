from moviepy.editor import VideoFileClip

# Открытие видеофайла
video_clip = VideoFileClip("example_video.mp4")

# Извлечение длительности видео
duration = video_clip.duration

# Извлечение размеров видео (ширина и высота)
width,height = video_clip.size

# Вывод информации
print(f"Длительность видео: {duration} секунд")
print(f"Размеры видео: {width}x{height} пикселей")

# Закрытие видеофайла
video_clip.close()