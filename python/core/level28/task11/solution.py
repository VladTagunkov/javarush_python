import matplotlib.pyplot as plt

# Данные для первой линии
x1 = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]

# Данные для второй линии
x2 = [1, 2, 3, 4, 5]
y2 = [2, 4, 6, 8, 10]

# Создание графика
plt.plot(x1,y1,label='Series A')
plt.plot(x2,y2,label='Series B')

# Добавление легенды
plt.title("Sample Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

# Отображение графика
plt.show()