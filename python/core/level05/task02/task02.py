# Ожидание стопа

# Напишите программу, которая создает пустой список с использованием квадратных скобок [] и добавляет в него элементы, запрашиваемые у пользователя.
# Ввод элементов должен продолжаться до тех пор, пока пользователь не введет слово "стоп". Затем программа должна вывести итоговый список.

# Напишите тут ваш код
res=[]

while True:
    inp = input()
    if inp=='стоп':break 
    res.append(inp) 
    
print(res)
    