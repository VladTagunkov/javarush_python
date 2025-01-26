import tkinter as tk

def on_button_click():
    print(":(")

# Создание основного окна
window = tk.Tk()


# Добавление метки
label = tk.Label(window,text="Добро пожаловать в приложение")
label.pack()

# Добавление кнопки
def on_button_click():
    label.config(text = "Кнопка была нажата")
    
button = tk.Button(window,text="Нажми меня", command=lambda: print("Кнопка была нажата"))
button.pack()

# Запуск главного цикла приложения
window.mainloop()