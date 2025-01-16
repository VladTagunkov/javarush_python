# Обработка ошибок при работе с файлами

# Напишите программу, которая открывает файл example.txt в режиме добавления, записывает в него строку "Новая линия.".
# Нужно корректно обрабатывать исключение FileNotFoundError, закрывая файл в любом случае.

# Напишите тут ваш код
tf=None
try:
    tf = open("example.txt","a")
    tf.write("Новая линия.")
except FileNotFoundError as e:
    print(f"Exception {e}")
finally:
    if tf is not None:
        tf.close()