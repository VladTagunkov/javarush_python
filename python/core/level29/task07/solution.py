from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph

# Пример данных для таблицы
data = [
    ["Месяц", "Продажи"],
    ["Январь", "$1000"],
    ["Февраль", "$1500"],
    ["Март", "$2000"]
]

# Имя PDF-файла для сохранения отчета
file_name = "sales_report.pdf"

# Создание PDF-документа
pdf = SimpleDocTemplate(file_name, pagesize=letter)

# Создание стиля и заголовка
styles = getSampleStyleSheet()
title = Paragraph("Отчет о продажах", styles['Title'])

# Создание таблицы с данными
table = Table(data)

# Применение стилей к таблице
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),           # Фон заголовка таблицы
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),      # Цвет текста в заголовке
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),                  # Выравнивание текста по центру
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),        # Шрифт заголовка
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),                 # Отступ снизу для заголовка
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),         # Фон для строк таблицы
    ('GRID', (0, 0), (-1, -1), 1, colors.black)             # Сетка для всей таблицы
])
table.setStyle(style)

# Сборка PDF с элементами
elements = [title,table]
pdf.build(elements)