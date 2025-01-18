import PyPDF2

def merge_pdfs_with_bookmarks(pdf_files, output_file):
    # Создаем PdfMerger для объединения PDF
    pdf_merger = PyPDF2.PdfMerger()
    page_offset = 0

        # Открываем текущий PDF-файл
        for file in pdf_files:
            pdf_reader = PyPDF2.PdfReader(file)    
            # Получаем количество страниц текущего файла
            pages = pdf_reader.pages
            
            # Добавляем текущий PDF-файл к PdfMerger
            pdf_merger.append(file)
            
            # Добавляем закладку в начало этого PDF-файла
            pdf_merger.add_bookmark(file,page_offset)
            page_offset += len(pages)

    # Записываем результат в выходной файл
    with open(output_file,'wb') as out_file:
        pdf_merger.write(out_file)

# Задаем имена входных и выходного файлов
input_files = ["part1.pdf", "part2.pdf", "part3.pdf"]
output_file = "merged_with_bookmarks.pdf"

# Запускаем функцию для объединения PDF с закладками
merge_pdfs_with_bookmarks(input_files, output_file)