from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet

# Имя файла для сохранения PDF
file_name = "simple_report.pdf"

# Создаем PDF-документ
c = canvas.Canvas(file_name,pagesize=letter)

# Устанавливаем стили для текста
text = c.beginText(40,750)
text.setFont("Helvetica",16)

# Добавляем заголовок
text.textLine("Ежедневный отчет")

# Добавляем подзаголовок
text.textLine("Состояние на сегодня")

# Сохраняем PDF-документ
c.drawText(text)
c.save()

    