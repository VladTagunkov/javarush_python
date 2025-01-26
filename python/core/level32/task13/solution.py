import tkinter as tk

# Создаем основное окно приложения
root = tk.Tk()
root.title("Main App.")

# Первая метка
label1 = tk.Label(root,text="Добро пожаловать!",font=("Arial",14),fg='green')
label1.pack()

# Вторая метка
label2 = tk.Label(root,text="Учебное приложение",font=("Courier",12),fg='blue')
label2.pack()

# Третья метка
label3 = tk.Label(root,text="Завершение работы",font=("Times",16),fg='red')
label3.pack()

# Запуск основного цикла приложения
root.mainloop()