# Чтение файла.

# Напишите программу, которая открывает файл example.txt для чтения, читает его содержимое и выводит его на экран.
# После этого закройте файл.

# Напишите тут ваш код
tf = open('example.txt','r')
print(tf.read())
tf.close()