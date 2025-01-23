from moviepy.editor import ColorClip

# Создаем клип синего цвета размером 640x360 пикселей и длительностью 10 секунд
blank_clip = ColorClip(size=(640,360), color=[0,0,255],duration=10)

# Устанавливаем частоту кадров 24 FPS
blank_clip.write_videofile("blue_clip.mp4", fps=24)

# Сохраняем клип в файл blue_clip.mp4
