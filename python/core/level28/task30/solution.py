import plotly.graph_objects as go
import pandas as pd

# Пример данных из предыдущей задачи
# Предположим, что в предыдущей задаче использовались временные ряды с датами и значениями
data = {
    'date': pd.date_range(start='2021-01-01', periods=100, freq='D'),
    'value': pd.Series(range(100)) + (pd.Series(range(100)) * 0.1).cumsum()
}

# Преобразуем данные в DataFrame
df = pd.DataFrame(data)

# Создаем фигуру с помощью Plotly
fig = px.line(data, x='date', y='value')

# Добавляем линию на график


# Настраиваем оси


# Добавляем возможность зума и панорамирования
fig.update_layout(xaxis=dict(rangeslider=dict(visible=True)),
                        title=dict(x=0.5))

# Показываем график
fig.show()