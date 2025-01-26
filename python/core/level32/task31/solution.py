import tkinter as tk
from tkinter import ttk

def show_selections():
    checkbox_status = "Активирован" if checkbox_var.get() else "Не активирован"
    season = season_var.get()
    number = scale_var.get()

    result = f"Чекбокс: {checkbox_status}, Сезон: {season}, Число: {number}"
    result_label.config(text=result)

# Создание главного окна
root = tk.Tk()
root.title("Приложение с элементами управления")

# Чекбокс
checkbox_var = tk.IntVar()
checkbox = tk.Checkbutton(root, text="Активировать",variable=checkbox_var)
checkbox.pack()

# Радиокнопки
season_var = tk.StringVar()
radio1 = tk.Radiobutton(root, text = "Лето",variable=season_var,value="Лето")
radio2 = tk.Radiobutton(root, text = "Осень",variable=season_var,value="Осень")
radio3 = tk.Radiobutton(root, text = "Зима",variable=season_var,value="Зима")
radio1.pack()
radio2.pack()
radio3.pack()


# Переключатель
scale_var = tk.Spinbox(root,from_=1, to=5)
scale_var.pack()

# Кнопка для отображения выбора
show_ = tk.Button(root,text="Show",command=show_selections)
show_.pack()

# Метка для отображения текущих выборов
result_label = tk.Label(root,text="")
result_label.pack()

# Запуск главного цикла
root.mainloop()
