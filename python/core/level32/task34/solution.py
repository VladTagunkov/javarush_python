import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import subprocess

# Функция для выбора файла с помощью диалога
def select_file():
    result_area.delete(1.0, tk.END)
    file_path = filedialog.askopenfilename(title="Choose file to run")
    global file_path_var
    file_path_var.set(file_path)
    result_area.configure(state='normal')
    result_area.insert(f"Путь: {file_path}")

    if file_path:
        return file_path


# Функция для выполнения выбранного скрипта
def execute_script():
    result_area.delete(1.0, tk.END)
    file_path = file_path_var.get()

    try:
        # Запускаем скрипт и захватываем вывод
        result = subprocess.run(['python', file_path],capture_output=True, text=True)
        result_area.configure(state='normal')
        result_area.insert(f"Скрипт выполнен успешно!\n\n{result.stdout}")

    except Exception as e:
        output = str(e)  # В случае ошибки выводим текст ошибки

    # Отображаем результат выполнения в текстовом поле
        result_area.configure(state='normal')
        result_area.insert(f"Скрипт выполнен не успешно!\n\n{result.stderr}")

# Создаем основное окно
root = tk.Tk()
root.title("Script Runner")  # Заголовок окна

# Переменная для хранения пути к файлу
file_path_var = tk.StringVar()


# Кнопка "Выбрать файл"
select_button = tk.Button(root, text="Выбрать файл", command=select_file)
select_button.grid(row=0, column=0, padx=5, pady=5)

# Поле для отображения пути к выбранному файлу
file_path_entry = tk.Entry(root, textvariable=file_path_var, width=50)
file_path_entry.grid(row=0, column=1, padx=5, pady=5)

# Кнопка "Запустить скрипт"
run_button = tk.Button(root, text="Запустить скрипт", command=execute_script)
run_button.grid(row=0, column=2, padx=5, pady=5)

# Текстовое поле с прокруткой для отображения вывода скрипта
result_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', width=60, height=15)
result_area.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Запуск основного цикла обработки событий
root.mainloop()
