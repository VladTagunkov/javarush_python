import PyPDF2

def merge_pdfs(file1, file2, output):
    # Открываем первый PDF файл
    with open(file1,'rb') as file_1:
        readed_1 = PyPDF2.PdfReader(file_1)

        # Открываем второй PDF файл
        with open(file2, 'rb') as file_2:
            reader_2 = PyPDF2.PdfReader(file_2)

            # Создаем объект для записи объединенного PDF
            writer = PyPDF2.PdfWriter()

            # Добавляем страницы из первого PDF в итоговый файл
            for i in range(len(readed_1.pages)):
                writer.add_page(readed_1.pages[i])

            # Добавляем страницы из второго PDF в итоговый файл
            for j in range(len(readed_2.pages)):
                writer.add_page(readed_2.pages[j])

            # Записываем объединенный PDF в выходной файл
            with open(output,'wb') as out_file:
                writer.write(out_file)

# Указываем имена исходных файлов и имя итогового файла
file1 = 'report_part1.pdf'
file2 = 'report_part2.pdf'
output_file = 'full_report.pdf'

# Объединяем PDF файлы
merge_pdfs(file1, file2, output_file)