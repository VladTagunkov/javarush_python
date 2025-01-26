import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    file_path = filedialog.askopenfilename(
        title="Открыть файл",
        filetypes = [("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
    if file_path:
        print(file_path)
        show_info(file_path)
        return file_path


def save_file():
    file_path = filedialog.asksaveasfilename(
        title="Сохранить файл",
        defaultextension = '.txt',
        filetypes = [("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
    if file_path:
        print(file_path)
        show_info(file_path)
        return file_path


def show_info(path_):
    messagebox.showinfo("Путь",path_)



# Создание главного окна приложения
root = tk.Tk()
root.title("Файл менеджер")

file_path_var = tk.StringVar()
save_path_var = tk.StringVar()

# Кнопка для открытия файла
open_button = tk.Button(root, text="Открыть файл", command=open_file)
open_button.pack(pady=10)

# Кнопка для указания пути сохранения файла
save_button = tk.Button(root, text="Сохранить файл", command=save_file)
save_button.pack(pady=10)


root.mainloop()