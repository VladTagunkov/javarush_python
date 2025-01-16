import matplotlib.pyplot as plt

# Данные: количество дней по месяцам
days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Месяцы от 1 до 12
months = [1,2,3,4,5,6,7,8,9,10,11,12]

# Построение графика
plt.plot(months, days_in_months, marker='o')

# Подписи осей
plt.xlabel('Месяц')
plt.ylabel('Количество дней')

# Заголовок графика
plt.title('Количество дней в каждом месяце')

# Отображение графика
plt.grid(True)
plt.show()