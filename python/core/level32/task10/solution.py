import tkinter as tk

def show_text():
    # Получаем текст из поля ввода
    entered_text = entry.get()
    # Выводим текст в консоль
    print(entered_text)

# Создаем главное окно приложения
root = tk.Tk()
root.title('My App')

# Создаем поле ввода
entry = tk.Entry()
entry.pack()

# Создаем кнопку и связываем ее с функцией show_text
button = tk.Button(root,text="Показать",command=show_text)
button.pack()

# Запускаем главный цикл приложения
root.mainloop()
