from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Загрузка видео
video = VideoFileClip("sample_video.mp4")

# Создание текстового клипа
txt_clip = TextClip("Important Announcement",fontsize=50, color='yellow', 
                    fontfamily='Arial')

# Установка позиции текста в верхней части видео
txt_clip = txt_clip.set_position('top')

# Наложение текстового клипа на видео
video_text = CompositeVideoClip([video,txt_clip])

# Сохранение результата
video_text.write_videofile("video_with_styled_text.mp4",fps=24)
