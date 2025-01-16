# Копирование файла

# Напишите программу, которая копирует файл source.txt в файл destination.txt

# Напишите тут ваш код
try:
    with open("source.txt","r") as source_file:
        sd = source_file.read()
        
    with open("destination.txt","w") as dest_file: 
        dest_file.write(sd)
except:
    print("Something wrong!")