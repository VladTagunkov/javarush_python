from moviepy.editor import VideoFileClip

def transform_video(input_file, output_file):
    # Загружаем видео
    clip = VideoFileClip(input_file)
    
    # Изменяем размер видео до 75% от исходного
    resized_clip = clip.resize(0.75)
    
    # Поворачиваем видео на 180 градусов
    rotated_clip = resized_clip.rotate(180)
    
    # Сохраняем преобразованное видео
    rotated_clip.write_videofile(output_file, codec='libx264')

# Определяем входной и выходной файлы
input_video = "sample_video.mp4"
output_video = "transformed_video.mp4"

# Выполняем трансформацию видео
transform_video(input_video, output_video)