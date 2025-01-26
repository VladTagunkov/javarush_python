import tkinter as tk

# Функция для вывода приветствия
def greet():
    print("Здравствуйте!")


# Функция для вывода прощания
def farewell():
    print("До встречи!")


# Функция для закрытия окна
def close_window():
    root.destroy()


# Создаем главное окно
root = tk.Tk()
root.title("Main App.")


# Добавляем кнопки
button_hi = tk.Button(root,text="Привет",command=greet)
button_fa = tk.Button(root,text="До свидания",command=farewell)
button_close = tk.Button(root,text="Закрыть",command=close_window)


# Размещаем кнопки в окне с отступами
button_hi.pack(pady=10)
button_fa.pack(pady=10)
button_close.pack(pady=10)

# Запускаем главный цикл обработки событий
root.mainloop()
