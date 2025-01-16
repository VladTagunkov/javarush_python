import matplotlib.pyplot as plt

# Подготовка данных для осей X и Y
     # Порядковые номера президентов от 1 до 47
    # 0 для первых 43 президентов и 1 для 44 и последующих
x = list(range(1,47))
y = [0]*43+[1]*(47-43)
# Построение графика
plt.plot(x, y, marker='o')

# Установка названия графика и подписей к осям
plt.title('Чёрные президенты США')
plt.xlabel('Номер президента')
plt.ylabel('Количество чёрных президентов')

# Отображение графика
plt.show()