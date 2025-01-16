import matplotlib.pyplot as plt

# Данные для графика
x_data = [0, 1, 2, 3, 4, 5]
y_data = [0, 1, 4, 9, 16, 25]

# Создание графика
plt.plot(x_data,y_data,linestyle='--',color='red',marker='o')

# Настройка заголовка и подписей осей
plt.title("Sample Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Отображение графика
plt.show()