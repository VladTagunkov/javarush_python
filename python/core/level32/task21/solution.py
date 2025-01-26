import tkinter as tk

# Создаем основное окно приложения
root = tk.Tk()

# Создаем три кнопки
button1 = tk.Button(root,text = "Кнопка 1")
button2 = tk.Button(root,text = "Кнопка 2")
button3 = tk.Button(root,text = "Кнопка 3")

# Размещаем кнопки вертикально друг под другом с использованием метода pack
button1.pack()
button2.pack()
button3.pack()

# Запускаем главный цикл обработки событий
root.mainloop()