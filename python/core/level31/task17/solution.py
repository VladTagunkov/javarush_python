from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Загрузка исходного видео
video = VideoFileClip("sample_video.mp4")            

# Создание текста
txt_clip = TextClip("Hello, World!",fontsize=20,color='red')

# Размещение текста на видео
txt_clip = txt_clip.set_duration(video.duration)
txt_clip = txt_clip.set_position('center')

# Сохранение изменённого видео
video_text = CompositeVideoClip([video,txt_clip])
video_text.write_videofile("output_with_text.mp4",fps=24)