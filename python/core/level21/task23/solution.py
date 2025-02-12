import pandas as pd

# Создаем DataFrame с данными о продажах
data = {
    'Магазин': ['Магазин A', 'Магазин A', 'Магазин B', 'Магазин C', 'Магазин C', 'Магазин B', 'Магазин A'],
    'Категория': ['Электроника', 'Одежда', 'Одежда', 'Электроника', 'Одежда', 'Электроника', 'Одежда'],
    'Выручка': [200, 150, 300, 400, 200, 500, 100]
}

df = pd.DataFrame(data)
# Группировка данных по колонкам 'Магазин' и 'Категория'
df_vs = df.groupby(['Магазин','Категория']).agg(sum=('Выручка','sum'),mean=('Выручка','mean'))


# Переименование колонок для удобочитаемости

# Вывод результатов группировки на экран
print(df_vs)