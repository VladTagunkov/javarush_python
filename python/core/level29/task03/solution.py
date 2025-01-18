import PyPDF2

# Открываем PDF-файл для чтения в бинарном режиме
with open("sample.pdf", 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)

    # Извлечение текста с первой страницы
    page_first = reader.pages[0].extract_text()
    # Запись текста первой страницы в текстовый файл
    with open("first_page.txt",'w') as f_file:
        f_file.write(page_first)

    # Извлечение текста с последней страницы
    page_last = reader.pages[-1].extract_text()
    # Запись текста последней страницы в текстовый файл
    with open("last_page.txt",'w') as l_file:
        l_file.write(page_last)