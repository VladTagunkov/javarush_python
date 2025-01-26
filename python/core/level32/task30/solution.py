import tkinter as tk

def update_title():


# Создаем основное окно
root = tk.Tk()


# Создаем StringVar для отслеживания выбора пользователя
color_ = tk.StringVar()

def update_title():
    root.title(color_.get())

# Создаем радиокнопки для выбора цвета
red_ = tk.Radiobutton(root, text="Красный", variable=color_, value='Red', command=update_title)
green_ = tk.Radiobutton(root, text="Зеленый", variable=color_, value='Green', command=update_title)
blue_ = tk.Radiobutton(root, text="Синий", variable=color_, value='Blue', command=update_title)

# Размещаем радиокнопки в окне
red_.pack()
green_.pack()
blue_.pack()


# Запускаем главный цикл приложения
root.mainloop()