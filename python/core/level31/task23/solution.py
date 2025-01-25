from moviepy.editor import VideoClip, TextClip, ImageClip, CompositeVideoClip
from moviepy.video.fx.all import resize, vfx

# Параметры видео
video_duration = 7  # Длительность видео в секундах
video_size = (640, 480)  # Размер видео (ширина, высота)

# Функция для анимации текста
def animate_text(t):
    # Вычисление позиции текста в зависимости от времени
    x,y = lambda t: (video_size[0] + int((0 - video_size[0]) * t), 
                    0 + int((video_size[1] - 0) * t))
    
    return (x, y)

# Функция для анимации изображения
def animate_image(t):
    # Увеличение масштаба от 50% до 100%
    scale = lambda t: 0.5 + 0.5 * t
    return scale

# Создание текстового клипа
text_clip = TextClip("Diagonal Text", fontsize=40, color='white', font='Arial') \
    .set_duration(video_duration) \
    .set_position(animate_text)

# Создание клипа с изображением
# Предполагается, что файл star.png находится в той же директории, что и скрипт
image_clip = ImageClip("star.png").set_duration(video_duration).resize(0.5)
image_clip = image_clip.fx(vfx.resize, lambda t: animate_image(t)).set_position('center')

# Создание основного видео клипа с фоном
background_clip = VideoClip(lambda t: (0, 0, 0), duration=video_duration).set_size(video_size)

# Объединение клипов
final_clip = CompositeVideoClip([background_clip, text_clip, image_clip])

# Сохранение итогового видео
final_clip.write_videofile("output_task3.mp4", fps=24)