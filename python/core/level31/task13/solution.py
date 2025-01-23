from moviepy.video.io.VideoFileClip import VideoFileClip

# Путь к входному видеофайлу
video_path = "input_video.mp4"  # Замените на путь вашего видеофайла

# Загрузка видеофайла с помощью MoviePy
video = VideoFileClip(video_path)

# Определение длительности каждого сегмента
segment_duration = video.duration / 3

# Создание и сохранение каждого из трех сегментов
clip1 = video.subclip(0,segment_duration)
clip2 = video.subclip(segment_duration,segment_duration*2)
clip3 = video.subclip(segment_duration*2,segment_duration*3)

# Закрытие видеофайла
clip1.write_videofile("segment1.mp4")
clip2.write_videofile("segment2.mp4")
clip3.write_videofile("segment3.mp4")

video.close()
