import PyPDF2

# Функция для извлечения указанного диапазона страниц из PDF-файла
def extract_pages(input_pdf, output_pdf, start_page, end_page):
    # Открываем исходный PDF-файл для чтения
    with open(input_pdf,'rb') as pdf_file: 
        reader = PyPDF2.PdfReader(pdf_file)
        writer = PyPDF2.PdfWriter()

        # Проходим по страницам в указанном диапазоне
        for pg_num in range(start_page-1,end_page):
            page = reader.pages[pg_num]
            writer.add_page(page)

        # Сохраняем извлеченные страницы в новый PDF-файл
        with open(output_pdf,'wb') as out_file:
            writer.write(out_file)

# Пути к файлам
input_pdf_path = "sample.pdf"          # Исходный PDF-файл
output_pdf_path = "range_2_to_4.pdf"   # Выходной PDF-файл с выбранными страницами

# Вызов функции для извлечения страниц 2-4
extract_pages(input_pdf_path, output_pdf_path, 2, 4)
