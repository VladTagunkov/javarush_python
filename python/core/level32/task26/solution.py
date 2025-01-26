import tkinter as tk
from tkinter import messagebox

def on_exit():
    response = messagebox.askyesno("Выход", "Вы действительно хотите выйти?")
    if response:
        root.quit()


# Создаем основное окно приложения
root = tk.Tk()
root.title("Приложение с подтверждением выхода")

# Создаем кнопку "Выход"
exit_button = tk.Button(root, text="Выход", command=on_exit)
exit_button.pack(pady=20)

# Запускаем главный цикл обработки событий
root.mainloop()