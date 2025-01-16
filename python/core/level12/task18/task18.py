# Сериализация словаря в строку

# Напишите программу, которая сериализует словарь в строку с использованием модуля pickle,
# а затем десериализует этот словарь из строки.

import pickle

# Пример словаря для сериализации
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'Wonderland'
}


# Напишите тут ваш код
data_str = pickle.dumps(data)
des = pickle.loads(data_str)

print(des)