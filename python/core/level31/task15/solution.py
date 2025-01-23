from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip

# Загрузка видеофрагментов
video1 = VideoFileClip("video1.mp4")
video2 = VideoFileClip("video2.mp4")
video3 = VideoFileClip("video3.mp4")

# Объединение видеофрагментов
fin = concatenate_videoclips([video1,video2,video3])

# Загрузка аудиофайла
audio = AudioFileClip('file_audio.mp3')

# Объединение видео с аудиосопровождением
fin_audio = fin.set_audio(audio)

# Сохранение конечного видео
fin_audio.write_videofile("video_with_audio.mp4")