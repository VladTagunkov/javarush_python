from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Загрузка исходного видео
video = VideoFileClip("sample_video.mp4")

# Создание первого текстового клипа "Welcome to the show!"
txt_clip1 = TextClip("Welcome to the show!",fontsize=10).set_position('bottom').set_duration(3)
txt_clip2 = TextClip("Enjoy watching!",fontsize=10).set_position('bottom').set_duration(3)


subs = [{"text":"Welcome to the show!","start":0,"end":3},
       {"text":"Enjoy watching!","start":5,"end":8}]

sub_clip = [TextClip(sub['text'], fontsize=20, color='red')
             .set_position(('center', 'bottom'))
             .set_start(sub['start'])
             .set_duration(sub['end'] - sub['start'])
             for sub in subs]

# Создание второго текстового клипа "Enjoy watching!"


# Комбинирование видео и текстовых клипов
video_sub = CompositeVideoClip([video]+sub_clip)

# Сохранение конечного видео с субтитрами
video_sub.write_videofile("output_with_subtitles.mp4")