import pdfplumber
import csv

# Задаем пути к PDF-файлу и CSV-файлу для сохранения результата
pdf_path = 'example.pdf'  # Укажите путь к вашему PDF-файлу
csv_path = 'output.csv'   # Укажите путь для сохранения CSV-файла

# Извлечение текста из PDF по страницам
with pdfplumber.open(pdf_path) as in_file:
    with open(csv_path, 'wb') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for page in in_file.pages:
            txt = page.extract_text()
            wr.writerow([txt])