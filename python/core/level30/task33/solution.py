from PIL import Image
from PIL.ExifTags import TAGS

# Ввод пути к изображению
image_path = input("Введите путь к изображению: ")

try:
    # Открываем изображение и пытаемся получить EXIF-данные
    with Image.open(image_path) as img:
        exif_data = img._getexif()
        # date_time = None
        # orientation = None 
        # x_resolution = None
        # y_resolution = None
        if exif_data is not None:
            date_time = None
            orientation = None 
            x_resolution = None
            y_resolution = None
        else:
            print("EXIF-данные не найдены.")
        
        for tag_id,value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            
            if tag == "DateTime":
                date_time = value
            elif tag == "Orientation":
                orientation = value
            elif tag == "XResolution":
                x_resolution = value
            elif tag == "YResolution":
                y_resolution = value
                    
            
            # Извлечение и отображение определенных EXIF-данных


        print(f"Дата и время съемки: {date_time}")
        print(f"Ориентация: {orientation}")
        print(f"Разрешение X: {x_resolution}")
        print(f"Разрешение Y: {y_resolution}")



except IOError:
    print("Ошибка при открытии изображения. Проверьте путь к файлу.")
