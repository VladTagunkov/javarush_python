from moviepy.editor import VideoFileClip
from PIL import Image

# Открываем видеофайл
video = VideoFileClip("input_video.mp4")

# Извлекаем кадр на пятой секунде
frame = video.get_frame(5)

# Преобразуем кадр в изображение PIL
img = Image.fromarray(frame)

# Сохраняем изображение в формате PNG
img.save("frame_5.png")