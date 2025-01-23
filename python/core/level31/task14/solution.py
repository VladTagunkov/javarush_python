from moviepy.editor import VideoFileClip, concatenate_videoclips

# Пути к исходным видеофайлам
video_paths = ["clip1.mp4", "clip2.mp4", "clip3.mp4"]

# Путь для сохранения конечного объединенного видео
output_path = "compiled_video.mp4"

# Загрузка видеоклипов
video0 = VideoFileClip(video_paths[0])
video1 = VideoFileClip(video_paths[1])
video2 = VideoFileClip(video_paths[2])


# Объединение клипов без переходов
fin = concatenate_videoclips([video0,video1,video2])

# Сохранение конечного видео в формате MP4
fin.write_videofile(output_path)

# Закрытие всех клипов для освобождения ресурсов
video0.close()
video1.close()
video2.close()
