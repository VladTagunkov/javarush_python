from moviepy.editor import TextClip, VideoClip

# Параметры клипа
text = "Horizontal Move"
duration = 5
video_width = 640
video_height = 480

# Создаем текстовый клип
text_clip = TextClip(text, fontsize=70, color='white', size=(video_width, video_height))

# Определяем начальную и конечную позиции текста
start_pos = -text_clip.width
end_pos = video_width

# Устанавливаем анимацию движения текста от левого края к правому с помощью set_position
pos_t_duration_center_ = pos_t_duration_center_ = lambda t: (start_pos + int((end_pos - start_pos) * (t / duration)), 'center')
animated_text = text_clip.set_position(pos_t_duration_center_).set_duration(duration)

# Создаем пустой фоновый видеоклип и накладываем на него текст с анимацией
animated_clip = VideoClip(lambda t: animated_text.get_frame(t), duration=duration)

# Сохраняем анимацию в файл
animated_clip.write_videofile("output_task2.mp4", fps=24)