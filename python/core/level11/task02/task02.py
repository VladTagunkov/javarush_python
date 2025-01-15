# Динамический импорт модуля

# Напишите программу, которая запрашивает у пользователя название модуля для импорта
# и имя функции для вызова из этого модуля.
# Программа должна динамически импортировать модуль и вызвать указанную функцию с любым аргументом.
# Для получения дочернего элемента у модуля используйте функцию getattr

# Напишите тут ваш код
mod = input("Enter modul name you want to import: ")
func = input("Enter function name you want to import: ")

imported_module = __import__(mod)
imported_fun = getattr(imported_module,func)

print(imported_fun(5))