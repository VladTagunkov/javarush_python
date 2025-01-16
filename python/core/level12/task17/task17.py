# Сериализация списка в файл

# Напишите программу, которая сериализует список в файл с использованием модуля pickle,
# а затем десериализует этот список из файла.

import pickle

# Пример списка для сериализации
data = [1, 2, 3, 'a', 'b', 'c']


# Напишите тут ваш код
with open("ful.pkl","wb") as file:
    pickle.dump(data,file)
    
with open("ful.pkl","rb") as file:
    res = pickle.load(file)
    
print(res)