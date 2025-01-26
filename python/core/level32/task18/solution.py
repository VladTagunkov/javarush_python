import tkinter as tk

def on_button_click():
    global click_count
    click_count += 1 
    button.config(text=f"Нажатие {click_count}")
    print(f"Нажатие {click_count}")


# Создание основного окна приложения
root = tk.Tk()
root.title("Кнопка-счетчик")

# Инициализация счетчика нажатий
click_count = 0

# Создание кнопки с начальным текстом
button = tk.Button(root, text="Нажми меня", command=on_button_click)
button.pack(padx=20, pady=20)

# Запуск основного цикла приложения
root.mainloop()