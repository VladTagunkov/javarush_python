import plotly.graph_objects as go

# Исходные данные
days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
water_levels = [2.5, 3.0, 3.5, 3.8, 3.2, 2.9, 3.1]

# Создание линейного графика
fig = go.Figure(data=go.Scatter(x=days_of_week,y=water_levels, mode='lines+markers'))

# Добавление линии на график
fig.update_layout(title="Water levels by days",
                  xaxis_title="Day of week",
                  yaxis_title="Water Level",
                  hovermode='closest')

# Добавление заголовка и меток осей


# Показать интерактивный график
fig.show()