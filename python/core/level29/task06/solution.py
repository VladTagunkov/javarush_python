import pdfplumber

# Укажите путь к вашему PDF-файлу
pdf_path = "example.pdf"

# Открытие PDF-файла с помощью PDFPlumber
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        table = page.extract_table()
        if table:
            for row in table:
                print(row)

    # Проход по каждой странице PDF-файла

        # Извлечение таблиц с текущей страницы

            # Вывод каждой строки таблицы в виде списка

