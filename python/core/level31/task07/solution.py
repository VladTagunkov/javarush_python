from moviepy.editor import VideoFileClip, AudioFileClip

# Открытие видеофайла и аудиофайла
video = VideoFileClip("example_video.mp4")
audio = AudioFileClip("background_music.mp3")

# Обрезка аудиодорожки до длины видео
audio_trim = audio.subclip(0,video.duration)

# Добавление аудиодорожки к видео
new_vid = video.set_audio(audio_trim)

# Сохранение результирующего видео
new_vid.write_videofile("video_with_music.mp4")