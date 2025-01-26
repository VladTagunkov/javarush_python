import tkinter as tk

def on_button_click():
    print("Привет, мир!")

# Создаем главное окно
root = tk.Tk()
root.title("Main Title!")

    

# Создаем кнопку с текстом "Привет"
button = tk.Button(root, text="Привет", command=on_button_click)

# Размещаем кнопку в окне
button.pack()

# Запуск основного цикла обработки событий
root.mainloop()