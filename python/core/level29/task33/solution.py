from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

# Имя выходного файла
filename = "output.pdf"

# Указание размеров страницы A4
width, height = A4
# Заголовок и текст
title = "Заголовок"
text = "Это пример текста, который будет центрирован на странице."

# Создание PDF-файла
pdf_file = canvas.Canvas(filename,pagesize=A4)
width, height = A4

# Шрифт и размер текста для заголовка
pdf_file.setFont('Helvetica-Bold',24)

# Вычисление позиций для центрирования заголовка
pdf_file.drawCenteredString(width/2, height-100,title)

# Отрисовка заголовка


# Шрифт и размер текста для абзаца
pdf_file.setFont('Helvetica',14)

# Вычисление позиций для центрирования текста
pdf_file.drawCenteredString(width/2, height-200,text)

# Отрисовка текста


# Завершение и сохранение PDF
pdf_file.save()
