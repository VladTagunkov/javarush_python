from moviepy.editor import VideoClip, TextClip, CompositeVideoClip, ColorClip

# Параметры текста
text = "Hello World"
fontsize = 70
color = 'white'
duration = 10
video_size = (640, 480)

# Создаем текстовый клип
text_clip = TextClip(text,color=color,fontsize=fontsize)

# Настраиваем длительность и позицию текстового клипа
text_clip = text_clip.set_position('center').set_duration(10)

# Создаем пустой видеоклип с указанным размером и длительностью
empty_clip = ColorClip(size=video_size,color="black").duration(duration)

# Накладываем текстовый клип на видеоклип
final_video = CompositeVideoClip([empty_clip,text_clip])

# Сохраняем финальный клип в файл
final_video.write_videofile("output_task1.mp4")