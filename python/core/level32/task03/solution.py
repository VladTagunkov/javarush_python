import tkinter as tk

# Создание основного окна
root = tk.Tk()

# Установка заголовка окна
root.title("Простое приложение c Label")

# Задание размеров окна
root.geometry("500x300")

# Создание и добавление Label в окно
label = tk.Label(root,text="Нажми меня")
label.pack(expand=True)  # Размещение метки в центре окна

# Запуск основного цикла приложения
root.mainloop()