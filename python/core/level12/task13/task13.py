# Создание и удаление директорий

# Напишите программу, которая создает новую директорию new_directory.
# Затем создает вложенную директорию parent_directory/child_directory.
# А затем удаляет созданные директории.

import os
import shutil

# Создание директории new_directory
# Напишите тут ваш код
os.mkdir("new_directory")

# Создание вложенной директории parent_directory/child_directory
# Напишите тут ваш код
os.makedirs("parent_directory/child_directory")
# Удаление директории new_directory
# Напишите тут ваш код
os.rmdir("new_directory")
# Удаление вложенной директории parent_directory/child_directory
# Напишите тут ваш код
if os.path.exists("parent_directory/child_directory")
    shutil.rmtree("parent_directory/child_directory")
else:
    print("dir not exists")