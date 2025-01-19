from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Имя выходного файла
filename = "report.pdf"

# Создание PDF-документа и установка размера страницы
pdf_file = canvas.Canvas(filename,pagesize=A4)
width, height = A4

# Первая страница с заголовком "Отчет 2023"
pdf_file.setFont('Helvetica',12)
pdf_file.drawString(100, height - 100, "Отчет 2023")
pdf_file.showPage()

# Вторая страница с текстом "Содержание"
pdf_file.setFont('Helvetica-Bold',14)
pdf_file.drawString(100, height - 100, "Содержание")
pdf_file.showPage()

# Третья страница с текстом "Конец отчета"
pdf_file.setFont('Times-Roman',16)
pdf_file.drawString(100, height - 100, "Конец отчета")
pdf_file.showPage()

# Сохранение документа
pdf_file.save()

