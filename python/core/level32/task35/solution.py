import tkinter as tk
from tkinter import messagebox
import subprocess

# Функция для выполнения скрипта
def run_script():

    try:
        result = subprocess.run(['python', 'run_script.py'], capture_output=True, text=True, check=True)
        output_text.insert(tk.END,text=f"Скрипт выполнен успешно!\n\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Ошибка выполнения", f"Возникла ошибка при выполнении скрипта:\n\n{e.stderr}")
        
    except Exception as ex:
        messagebox.showerror(f"We have error which is not usual as subprocess error - {ex}")


# Создаем главное окно
root = tk.Tk()
root.title("Запуск скрипта")

# Создаем текстовое поле для отображения вывода
output_text = tk.Text(root, wrap='word', width=80, height=20)
output_text.pack(padx=10, pady=10)

# Создаем кнопку для запуска скрипта
run_button = tk.Button(root, text="Запустить скрипт", command=run_script)
run_button.pack(pady=10)

# Запускаем главный цикл обработки событий
root.mainloop()