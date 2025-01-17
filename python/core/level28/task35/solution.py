import plotly.express as px
import pandas as pd

# Данные о продажах за каждый месяц
sales_data = {
    'Месяц': ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
    'Продажи': [1200, 1500, 1700, 1800, 1600, 2000, 2100, 1900, 2300, 2200, 2500, 2700]
}

# Создание DataFrame
data = pd.DataFrame(sales_data)

# Создание интерактивного линейного графика
fig = px.line(data, x='Месяц', y='Продажи', title="Sales data")

# Обеспечение функции зумирования
fig.update_layout(
    xaxis=dict(rangeslider=dict(visible=True)),
    title=dict(x=0.5)  # Центрирование заголовка
)

# Отображение графика
fig.show()