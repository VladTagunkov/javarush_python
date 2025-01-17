import matplotlib.pyplot as plt

# Данные для графика
x_values = list(range(6))
y_values = [x**2 for x in x_values]

# Создание линейного графика
plt.plot(x_values,y_values)

# Аннотирование осей
plt.xlabel("Число",fontsize=14,color='green')
plt.ylabel("Квадрат числа",fontsize=14,color='green')

# Настройка заголовка
plt.title("Квадрат чисел",fontsize=17,color='gray')

# Отображение графика
plt.show()