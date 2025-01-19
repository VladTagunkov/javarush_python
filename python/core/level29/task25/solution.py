import PyPDF2

# Запрашиваем у пользователя путь к PDF файлу
file_path = input("Введите путь к PDF-файлу: ")

# Открываем PDF файл в бинарном режиме для чтения
with open(file_path,'rb') as in_file:

    # Создаем PDF reader объект
    reader = PyPDF2.PdfReader(in_file)

    # Инициализируем переменную для хранения извлеченного текста
    text = ""

    # Проходим по всем страницам в PDF файле
    for page in reader.pages:
        text += page.extract_text()

        # Получаем страницу

        # Извлекаем текст из страницы


# Выводим извлеченный текст на экран
print(text)