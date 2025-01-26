import tkinter as tk

def clear_text():
    text_field.delete(1.0, tk.END)

# Создание главного окна
root = tk.Tk()
root.title("Main App")

# Создание текстового поля
text_field = tk.Text(root,height=10, width=40)
text_field.pack()

# Создание кнопки "Очистить"
button = tk.Button(root, text="Очистить", command=clear_text)
button.pack()

# Запуск основного цикла приложения
root.mainloop()