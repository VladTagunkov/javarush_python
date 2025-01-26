import tkinter as tk

# Создаем главное окно приложения
root = tk.Tk()
root.title("Main App")


def ext_():
    root.destroy()

# Создаем кнопки
but1 = tk.Button(root,text="Загрузить данные")
but2 = tk.Button(root,text="Построить график")
but3 = tk.Button(root,text="Выход",command=ext_)

# Размещаем кнопки в окне
but1.pack()
but2.pack()
but3.pack()

# Запускаем главный цикл обработки событий
root.mainloop()