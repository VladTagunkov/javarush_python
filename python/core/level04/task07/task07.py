# Круглый математик

# Напишите программу, которая запрашивает у пользователя вещественное число и округляет его вниз (с использованием math.floor()),
# вверх (с использованием math.ceil()) и до ближайшего целого числа (с использованием round()).
# Выведите результаты всех трех округлений.

# Напишите тут ваш код
import math 

num_ = float(input("Enter float: "))

num_fl = math.floor(num_)
num_ce = math.ceil(num_)
num_r = round(num_)

print(num_fl)
print(num_ce)
print(num_r)