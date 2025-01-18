from PyPDF2 import PdfReader, PdfWriter

# Функция для разделения PDF-файла на основе указанного диапазона страниц
def split_pdf(input_pdf, start_page, end_page, output_pdf):
    # Открываем входной PDF-файл для чтения
    with open(input_pdf,'rb') as in_file:

        # Вычисляем нулевые индексы для начальной и конечной страницы
        # Поскольку end_page включена, используем её как конец диапазона (исключительно)
        # if start_page==0:
        #     end_page -= 1
    
        # Добавляем страницы из указанного диапазона в объект writer
    
    
        # Записываем новый PDF-файл с выбранными страницами
        reader = PyPDF2.PdfReader(pdf_file)
        writer = PyPDF2.PdfWriter()

        # Проходим по страницам в указанном диапазоне
        for pg_num in range(start_page-1,end_page):
            page = reader.pages[pg_num]
            writer.add_page(page)

        # Сохраняем извлеченные страницы в новый PDF-файл
        with open(output_pdf,'wb') as out_file:
            writer.write(out_file)


# Пример использования
split_pdf('sample.pdf', 1, 3, 'section_1.pdf')  # Извлечение страниц 1–3
split_pdf('sample.pdf', 5, 7, 'section_2.pdf')  # Извлечение страниц 5–7
