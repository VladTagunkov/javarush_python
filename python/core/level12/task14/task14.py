# Получение списка файлов и директорий
# Напишите программу, которая выводит содержимое текущей рабочей директории и
# для каждого файла или директории указывает, является ли это файлом или директорией.
# Напишите тут ваш код
import os

cur_dir = os.getcwd() 

for elem in os.listdir(cur_dir):
    if os.path.isdir(elem):
        print(f"This is directory {elem}")
    elif os.path.isfile(elem):
        print(f"This is file {elem}")