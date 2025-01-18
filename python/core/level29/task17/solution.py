import PyPDF2

# Задаем имена входного и выходного файлов
input_pdf = "sample.pdf"
output_pdf = "page_1.pdf"

# Открытие PDF-документа для чтения
with open(input_pdf,'rb') as in_file:
    reader = PyPDF2.PdfReader(in_file)

    # Извлечение первой страницы
    page = reader.pages[0]

    # Создание нового PDF-объекта для записи
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)

    # Сохранение первой страницы в новый PDF-файл
    with open(output_pdf,'wb') as out_file:
        writer.write(out_file)
