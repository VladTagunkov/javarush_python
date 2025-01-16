# Чтение бинарного файла

# Напишите программу, которая читает бинарный файл example.bin и выводит его содержимое в консоль в виде байтов.

# Напишите тут ваш код
try:
    with open("example.bin","rb") as file:
        print(file.read())
except:
    print("Something was wrong!")