import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext

def load_file():
    # Открываем диалоговое окно для выбора файла
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Читаем содержимое файла
            content = file.read()
            # Отображаем содержимое в текстовом поле
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)

# Создаем главное окно
root = tk.Tk()
root.title("Main App")

# Создаем метку
label = tk.Label(root,text="Текстовый редактор")
label.pack()

# Создаем текстовое поле с полосой прокрутки
text_area = tk.Text(root,wrap='word')
text_area.pack(expand=1,fill='both')

# Создаем кнопку "Загрузить файл"
button = tk.Button(root,text="Загрузить файл",command=load_file)
button.pack()

# Устанавливаем начальный размер окна
