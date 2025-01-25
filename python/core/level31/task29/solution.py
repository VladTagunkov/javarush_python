from moviepy.editor import VideoFileClip, concatenate_videoclips

# Загрузка видеофайлов из текущей рабочей директории
video1 = VideoFileClip("video1.mp4")
video2 = VideoFileClip("video2.mp4")

# Определение продолжительности перехода
crossfade_duration = 1  # 1 секунда

# Настройка плавного перехода для второго клипа
video1 = video1.crossfadeout(1)
video2 = video2.crossfadein(1)

# Объединение видео с плавным переходом
fin_clip = concatenate_videoclips([video1,video2],method='compose')

# Сохранение результирующего видео
fin_clip.write_videofile("simple_crossfade.mp4")
