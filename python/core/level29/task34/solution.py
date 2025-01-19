from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.enums import TA_LEFT, TA_RIGHT

# Создаем PDF документ
doc = SimpleDocTemplate("styled_text.pdf", pagesize=letter)

# Стандартные стили
styles = getSampleStyleSheet()

# Создаем стиль для первого абзаца
style_first_paragraph = ParagraphStyle(fontName = 'Times-Roman',
                                       fontSize = 12,
                                       alignment = TA_LEFT)

# Создаем стиль для второго абзаца
style_second_paragraph = ParagraphStyle(fontName = 'Times-Italic',
                                       fontSize = 14,
                                       alignment = TA_RIGHT)

# Определяем текст для абзацев
text1 = "Это первый абзац, выровненный по левому краю, с шрифтом Times-Roman, размером 12."
text2 = "Это второй абзац, выровненный по правому краю, с шрифтом Times-Italic, размером 14."

# Создаем объекты Paragraph для каждого абзаца
paragraph1 = Paragraph(text1, style_first_paragraph)
paragraph2 = Paragraph(text2, style_second_paragraph)

# Добавляем абзацы в список элементов документа
elements = [paragraph1, paragraph2]

# Создаем PDF, добавляя в него элементы
doc.build(elements)