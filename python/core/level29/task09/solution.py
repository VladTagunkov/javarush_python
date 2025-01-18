import PyPDF2

# Укажите путь к вашему PDF-файлу
file_path = "example.pdf"

# Открываем PDF файл в режиме чтения
with open(file_path,'rb') as pdf_file:
    # Создаем объект PdfReader
    reader = PyPDF2.PdfReader(pdf_file)

    # Переменная для хранения текста со всех страниц
    text = ""

    # Проходим по всем страницам и извлекаем текст
    for elem in range(len(reader.pages)):
        page = reader.pages[elem]
        text += page.extract_text() + "\n"

# Вывод извлеченного текста на экран
print(text)
