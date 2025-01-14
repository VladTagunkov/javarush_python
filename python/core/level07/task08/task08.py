# Лига Плюща

# Напишите программу, которая создает словарь с информацией о студенте (имя, возраст, университет).
# Программа должна:
# Проверить наличие значения "MIT" с использованием метода values().
# Проверить наличие значения "Harvard" с использованием функции set().
# Проверить наличие значения 22 с использованием генератора.

# Напишите тут ваш код
student={'name':"Alex",'age':22,'university':"MIT"}

if "MIT" in student.values():
    print("MIT in dict")
else:
    print("MIT not in dict")
    
val_set = set(student.values())

if "Harvard" in val_set:
    print("Harvard in dict")
else:
    print("Harvard not in dict")
    
val=22 

if any(va==val for va in student.values()):
    print("Age is 22")
else:
    print("Other age")
    