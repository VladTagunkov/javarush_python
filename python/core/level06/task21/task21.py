# Очистка

# Напишите программу, которая принимает строку от пользователя и выполняет следующие операции:
# Удаляет пробелы в начале и конце строки с использованием метода strip().
# Преобразует все символы строки в нижний регистр с использованием метода lower().
# Преобразует все символы строки в верхний регистр с использованием метода upper().
# Выводит результаты каждой операции.

# Напишите тут ваш код
string = input()
st1 = string.strip()
st2 = st1.lower()
st3 = st2.upper()

print(st1)
print(st2)
print(st3)