# Мешанина

# Напишите программу, которая запрашивает у пользователя целое число, вещественное число и строку.
# Затем преобразуйте целое число в вещественное, вещественное число в строку, и строку в целое число (если это возможно).
# Выведите результаты преобразований и их типы.

# Напишите тут ваш код
int_ = int(input('Enter int number: '))
float_ = float(input("Enter float number: "))
str_ = input('Enter string: ')

int_float = float(int_)
float_string = str(float_)
str_int = int(str_)

print(int_float)
print(float_string)
print(str_int)
