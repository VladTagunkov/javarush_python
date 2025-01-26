import tkinter as tk

# Создаем главное окно приложения
root = tk.Tk()
root.title("Main App")

# Создаем кнопки
button1 = tk.Button(root, text = "Вверх")
button2 = tk.Button(root, text = "Вниз")
button3 = tk.Button(root, text = "Влево")
button4 = tk.Button(root, text = "Вправо")

# Размещаем кнопки с использованием метода pack
button1.pack(side=tk.TOP, fill=tk.X)
button2.pack(side=tk.BOTTOM, fill=tk.X)
button3.pack(side=tk.LEFT, fill=tk.Y)
button4.pack(side=tk.RIGHT, fill=tk.Y)

# Запуск основного цикла обработки событий
root.mainloop()