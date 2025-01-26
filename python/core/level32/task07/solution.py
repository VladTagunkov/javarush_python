import tkinter as tk

# Функция-обработчик нажатия кнопки
def button_click_handler():
    # Изменяем текст на метке при нажатии кнопки
    label.config(text=":(")

# Созда
root = tk.Tk()


# Создаем метку с начальным текстом
label = tk.Label(root,text="This is a button!")
label.pack(pady=10)  # Отступ сверху и снизу

def button_click_handler():
    label.config(text="Кнопка нажата")

# Создаем кнопку, привязывая к ней обработчик события
button = tk.Button(root, text = "Кнопка нажата", command= button_click_handler)
button.pack(pady=5)  # Отступ сверху и снизу

# Запускаем главный цикл окна
root.mainloop()
