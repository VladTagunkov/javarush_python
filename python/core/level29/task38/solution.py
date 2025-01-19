from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

# Путь для сохранения PDF
output_file = "report_with_table.pdf"

# Создание документа
doc = SimpleDocTemplate(output_file, pagesize=A4)
elements = []
# Стили для заголовков и текста
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'TitleStyle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=24,
    spaceAfter=12
)
subtitle_style = ParagraphStyle(
    'SubtitleStyle',
    parent=styles['Heading2'],
    fontName='Helvetica',
    fontSize=18,
    spaceAfter=12
)

# Заголовок и подзаголовок
title = Paragraph("Отчет о Продажах",title_style)
subtitle = Paragraph("За Первый Квартал",subtitle_style)
splitter = Spacer(1,20)

# Примерные данные для таблицы
data = [["Товар", "Регион", "Продажи"]]
sample_data = [["Товар A", "Север", "2000"], ["Товар B", "Юг", "1500"]]
data.extend(sample_data)  


# Создание таблицы и применение стилей
table = Table(data, colWidths=[5 * cm, 5 * cm, 4 * cm])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 12),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
]))

# Составление документа с элементами
elements.append(title)
elements.append(splitter)
elements.append(subtitle)
elements.append(table)

# Построение PDF

doc.build(elements)
print(f"Отчет сохранен как {output_file}")
