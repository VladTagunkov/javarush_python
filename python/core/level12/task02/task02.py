# Режимы доступа

# Напишите программу, которая создает или открывает файл example.txt в режиме записи и
# записывает в него строку "Hello, World!".
# Затем откройте файл в режиме добавления и добавьте строку "Appended text.".

# Напишите тут ваш код
tf = open("example.txt",'w')
tf.write("Hello, World!")
tf.close()
tf2 = open("example.txt",'a')
tf2.write("Appended text.")
tf2.close()