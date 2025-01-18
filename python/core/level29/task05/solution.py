import pdfplumber

# Путь к PDF-документу
pdf_path = 'test_document.pdf'

# Извлекаем и выводим текст с первой страницы
with pdfplumber.open(pdf_path) as pdf:
    page1 = pdf.pages[0]
    text_ = page1.extract_text()
    # Извлекаем текст с первой страницы
    print(text_)


