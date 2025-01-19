import pdfplumber
import pandas as pd

# Путь к PDF и Excel файлам
pdf_path = "example.pdf"  # Укажите путь к PDF-файлу
excel_path = "output.xlsx"  # Укажите путь для сохранения Excel-файла

# Извлечение таблицы из PDF
with pdfplumber.open(pdf_path) as pdf:
    tables = []
# Проверка наличия таблицы и сохранение в Excel
    for page in pdf.pages:
        table = page.extract_table()
        if table:
            tables.extend(table)
    # Конвертация таблицы в DataFrame
    df = pd.DataFrame(tables[1:],columns=tables[0])

    # Сохранение DataFrame в Excel файл
    df.to_excel(excel_path,index=False)

