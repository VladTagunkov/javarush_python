from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Spacer

# Имя файла для сохранения PDF документа
filename = "basic_report.pdf"

# Создаем новый PDF документ
doc = canvas.Canvas(filename,pagesize=letter)
width, height = letter

# Устанавливаем ширину и высоту страницы


# Добавляем заголовок
doc.setFont('Helvetica-Bold',18)
doc.drawString(100, height - 100,"Отчет о Продажах" )

# Добавляем разделитель
doc.drawString(105, height - 110,'--------------------------------')

# Добавляем подзаголовок
doc.setFont('Helvetica',16)
doc.drawString(100, height - 150,"За Первый Квартал" )

# Сохраняем PDF документ
doc.save()
