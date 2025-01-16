# Создание файла

# Напишите программу, которая создает новый файл example.txt и записывает в него строку "This is a new file."

# Напишите тут ваш код

tf = open('example.txt','w')
tf.write("This is a new file.\n")
tf.close()