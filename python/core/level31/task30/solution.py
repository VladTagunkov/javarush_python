from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip

# Загрузка видеоклипов
scene1 = VideoFileClip("scene1.mp4")
scene2 = VideoFileClip("scene2.mp4")

# Продолжительность перехода
fade_duration = 2

# Применение эффекта затемнения к "scene1"
scene1 = scene1.fadeout(fade_duration)
scene2 = scene2.fadein(fade_duration)

# Применение эффекта появления из темноты к "scene2"


# Объединение клипов с переходом
fin_clip = concatenate_videoclips([scene1,scene2],method='compose')

# Экспорт готового видеофайла
fin_clip.write_videofile("fade_to_black.mp4")