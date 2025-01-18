import PyPDF2

# Путь к PDF-файлу и выходному текстовому файлу
pdf_file = 'example.pdf'
output_file = 'extracted_text.txt'

# Чтение и извлечение текста из PDF-файла
with open(pdf_file,'rb') as pdf_file:
    # Создаем объект PdfReader
    reader = PyPDF2.PdfReader(pdf_file)

    # Переменная для хранения текста со всех страниц
    text = ""

    # Проходим по всем страницам и извлекаем текст
    for elem in range(len(reader.pages)):
        page = reader.pages[elem]
        text += page.extract_text() + "\n"


# Сохранение извлеченного текста в текстовый файл
with open(output_file,'w',encoding='utf-8') as out_file:
    out_file.write(text)