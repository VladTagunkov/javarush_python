from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Параметры страницы
width, height = A4

# Создание PDF-документа
pdf_file = canvas.Canvas('report.pdf',pagesize=A4)
width, height = A4

# Настройка текста
pdf_file.setFont('Times-Roman',14)

# Вычисление позиции для текста (верхняя четверть страницы)
pdf_file.drawString(100, height - (height/4+20), "Это мой первый PDF-документ")

# Настройка шрифта и вставка текста


# Сохранение PDF-документа
pdf_file.save()