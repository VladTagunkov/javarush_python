import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

def run_script():
    file_path = filedialog.askopenfilename(title="Choose file for run")
    if file_path:
        res = subprocess.run(['python',file_path],capture_output=True, text=True)
        messagebox.showinfo("Скрипт запущен!","Скрипт запущен!")
    # Открываем диалоговое окно для выбора файла

            # Запуск выбранного скрипта с использованием subprocess

            # Уведомление о запуске скрипта


# Создание основного окна приложения
root = tk.Tk()
root.title("Запуск скрипта")

# Создание и размещение кнопки "Запустить скрипт"
run_button = tk.Button(root, text="Запустить скрипт", command=run_script)
run_button.pack(pady=20)

# Запуск главного цикла обработки событий
root.mainloop()