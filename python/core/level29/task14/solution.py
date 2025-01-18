import PyPDF2

# Путь к исходным PDF-файлам и результирующему файлу
file1 = 'documentA.pdf'
file2 = 'documentB.pdf'
output = 'even_pages_merged.pdf'

# Создаем объект PdfWriter для объединенных страниц


# Обработка первого файла


# Обработка второго файла


# Запись объединенного PDF в выходной файл
in_file_list = [file1,file2]
pdf_writer = PyPDF2.PdfWriter()
# Открываем PDF-файлы
for fls in in_file_list:
    with open(fls,'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for pg in range(1,len(pdf_reader.pages),2):
            #if (pg+1) % 2 == 0 :
                page = pdf_reader.pages[pg]
                pdf_writer.add_page(page)
            
with open(output,"wb") as out_file:
    pdf_writer.write(out_file)

