from moviepy.editor import VideoFileClip

# Загрузка видеофайла
input_video_path = "input_video.mp4"
video_clip = VideoFileClip(input_video_path)

# Экспорт видео с использованием кодека H.264 и частотой кадров 24 fps
video_clip.write_videofile("basic_export.mp4",
                           codec = "H.264",
                           bitrate = "2000k",
                           fps = 24,
                           present = "medium")

# Закрытие файла с видео, чтобы освободить ресурсы
video_clip.quit()