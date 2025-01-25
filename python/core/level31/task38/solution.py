from moviepy.editor import VideoFileClip

# Путь к входному и выходному видеофайлам
input_path = "input_video.mp4"
output_path = "resized_video.mp4"

# Новые размеры видео и целевой FPS
new_width = 1280
new_height = 720
fps = 30

# Загрузка видеофайла
video = VideoFileClip(input_path)

# Изменение размера видео
res_vid = video.resize(1280,720)

# Экспорт видео с нужными параметрами
res_vid.write_videofile(output_path,
                        codec = "libx264",
                        bitrate = "2000k",
                        fps = 30,
                        preset = "medium")


print(f"Видео сохранено как {output_path} с разрешением {new_width}x{new_height} и частотой {fps} кадров в секунду.")
