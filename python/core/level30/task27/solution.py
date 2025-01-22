from PIL import Image

def apply_mask(foreground_path, mask_path, output_path):
    # Загрузка изображения и маски
    image = Image.open(foreground_path)
    mask = Image.open(mask_path).conver('L')

    # Изменение размера маски, чтобы она соответствовала изображению
    mask = mask.resize(image.size)

    # Применение маски к альфа-каналу изображения
    image.putalpha(mask)

    # Объединяем RGB и маску как альфа-канал


    # Сохранение результирующего изображения
    image.save(output_path)

apply_mask("foreground.png", "mask.png", "masked_result.png")
