import tkinter as tk

# Создание главного окна
root = tl.Tk()
root.title("Main App.")

# Создание кнопок
buttons = ["7", "8", 
          "9", "0"]
          
row_val = 0
col_val = 0

for button in buttons:
    btn = tk.Button(root, text=button, width=5)
    btn.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 1:
        col_val = 0
        row_val += 1
        
# Размещение кнопок с использованием метода grid


# Запуск основного цикла приложения
root.mainloop()