import PyPDF2

# Открытие PDF-документа

    # Создание PDF Reader объекта


    # Инициализация списка страниц для извлечения


    # Извлечение текста и вывод на экран
pdf_file = 'example.pdf'
#output_file = 'extracted_text.txt'

# Чтение и извлечение текста из PDF-файла
with open(pdf_file,'rb') as pdf_file:
    # Создаем объект PdfReader
    reader = PyPDF2.PdfReader(pdf_file)

    # Переменная для хранения текста со всех страниц
    text = ""

    # Проходим по всем страницам и извлекаем текст
    for elem in [1,3]:
        page = reader.pages[elem]
        text += page.extract_text() + "\n"


print(text)