from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

# Имя PDF-файла для создания
filename = "sectioned_report.pdf"

# Создание PDF-файла и установка размера страницы
c = canvas.Canvas(filename, pagesize=A4)

# Установка начальных координат
text = c.beginText(40,350)

# Добавление заголовка
text.textLine("Еженедельный отчет")

# Добавление подзаголовков
text.textLine("1. Общая информация")
text.textLine("2. Результаты анализа")
text.textLine("3. Прогнозы")

# Сохранение PDF-файла
c.drawText(text)
c.save()
