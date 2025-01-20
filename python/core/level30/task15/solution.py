from PIL import Image

def composite_images(image1_path, image2_path, mask_path, output_path):
    # Загрузка изображений и маски
    img1 = Image.open(image1_path)
    img2 = Image.open(image2_path)
    mask = Image.open(mask_path)

    # Проверка, что размеры изображений и маски совпадают
    if img1.size==img2.size==mask.size:
        print(True)
    else:
        print(False)

    # Создание композиции
    composit = Image.composite(img1,img2,mask)

    # Сохранение композиционного изображения
    composit.save(output_path)

# Пример использования функции
image1_path = 'image1.jpg'  # путь к первому изображению
image2_path = 'image2.jpg'  # путь ко второму изображению
mask_path = 'mask.png'      # путь к изображению маски
output_path = 'composited_image.jpg'  # путь для сохранения результата

composite_images(image1_path, image2_path, mask_path, output_path)