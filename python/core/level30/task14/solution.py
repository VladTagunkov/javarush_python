from PIL import Image

def blend_images(image_path1, image_path2, output_path, alpha=0.5):
    # Загрузка изображений
    img1 = Image.open(image_path1)
    img2 = Image.open(image_path2)

    # Проверка на одинаковый размер изображений
    if img1.size==img2.size:
        print(True)
    else:
        print(False)

    # Смешивание изображений с использованием метода blend()
    blend_img = Image.blend(img1,img2,alpha=alpha)

    # Сохранение результата
    blend_img.save(output_path)


# Путь к первым двум изображениям
image_path1 = 'image1.jpg'  # укажите путь к первому изображению
image_path2 = 'image2.jpg'  # укажите путь ко второму изображению

# Путь для сохранения смешанного изображения
output_path = 'blended_image.jpg'

# Смешивание изображений
blend_images(image_path1, image_path2, output_path)