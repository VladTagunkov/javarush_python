import PyPDF2

# Путь к исходным PDF-файлам и результирующему файлу
file1 = 'file1.pdf'
file2 = 'file2.pdf'
output = 'merged_document.pdf'

in_file_list = [file1,file2]
pdf_writer = PyPDF2.PdfWriter()
# Открываем PDF-файлы
for fls in in_file_list:
    with open(fls,'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for pg in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[pg]
            pdf_writer.add_page(page)
            
with open(output,"wb") as out_file:
    pdf_writer.write(out_file)

# Создаем объект PdfReader для каждого файла


# Создаем объект PdfWriter, который будет содержать объединенные страницы


# Извлекаем все страницы из первого PDF и добавляем их в PdfWriter


# Извлекаем все страницы из второго PDF и добавляем их в PdfWriter


# Сохраняем новый PDF файл


# Закрываем все открытые файлы
