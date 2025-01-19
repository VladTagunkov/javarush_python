from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

# Название файла PDF
pdf_file = "formatted_text.pdf"

# Создание PDF документа
doc = SimpleDocTemplate(pdf_file, pagesize=A4)
width, height = A4

# Использование стандартных стилей из ReportLab
styles = getSampleStyleSheet()

# Заголовок
title_style = ParagraphStyle(fontName = 'Helvetica-Bold',
                             fontSize = 18,
                             textColor='red')


# Стиль для абзацев
paragraph_style = ParagraphStyle(fontName = 'Helvetica',
                             fontSize = 12,
                             textColor='black')



# Заголовок и текст
title = "This is the Title"
first_paragraph = "This is the first paragraph of the document. It provides an introduction and overview of the topic being discussed."
second_paragraph = "This is the second paragraph of the document. It continues the discussion and provides additional insights and information."

# Создание элементов для документа
elements = []

# Добавление заголовка
elements.append(Paragraph(title, title_style))
elements.append(Spacer(1, 12))

# Добавление первого абзаца
elements.append(Paragraph(first_paragraph, paragraph_style))
elements.append(Spacer(1, 12))

# Добавление второго абзаца
elements.append(Paragraph(second_paragraph, paragraph_style))
elements.append(Spacer(1, 12))

# Составление PDF
doc.build(elements)