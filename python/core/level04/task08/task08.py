# Сравнивать очень просто

# Напишите программу, которая запрашивает у пользователя два вещественных числа и сравнивает их с использованием допустимой погрешности epsilon.
# Выведите результат сравнения на экран.

# Напишите тут ваш код

fl_1 = float(input("Enter float: "))
fl_2 = float(input("Enter float: "))
epsilon = 0.00000000000001

if abs(fl_1-fl_2) < epsilon:
    print('Equal')
else:
    print('Not Equal')

