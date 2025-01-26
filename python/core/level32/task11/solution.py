import tkinter as tk

def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        #result_label.config(text=f"Сумма: {result}")
        print(f"Сумма: {result}")
    except ValueError:
        print("Ошибка: пожалуйста, введите числовые значения.")


def multiply_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        #result_label.config(text=f"Result: {result}")

        print(f"Произведение: {result}")
    except ValueError:
        print("Ошибка: пожалуйста, введите числовые значения.")

# Создаем основное окно
root = tk.Tk()
root.title("Calculator")

# Поля ввода
entry1 = tk.Entry(root,width=10)
entry1.pack(pady=5)

entry2 = tk.Entry(root,width=10)
entry2.pack(pady=5)

# Кнопка "Сложить"
add_button = tk.Button(root,text="Сложить",command=add_numbers)
add_button.pack(pady=5)

# Кнопка "Умножить"
multiply_button = tk.Button(root,text="Умножить",command=multiply_numbers)
multiply_button.pack(pady=5)

# Запуск основного цикла приложения
root.mainloop()