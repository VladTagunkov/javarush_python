from moviepy.editor import VideoFileClip

# Загружаем исходное видео
input_path = "input_video.mp4"
video = VideoFileClip(input_path)

# Устанавливаем параметры для экспорта
output_path = "web_export.webm"
target_resolution = (854, 480)
target_bitrate = "1000k"
fps = 24

# Экспортируем видео в формате WebM с указанными параметрами
video.write_videofile(output_path,
                      codec = "libvpx-vp8",
                      fps=fps,
                      bitrate = target_bitrate,
                      resolution = target_resolution)