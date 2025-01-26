import tkinter as tk

def update_status():
    option1_status = "Включена" if var1.get() else "Выключена"
    option2_status = "Включена" if var2.get() else "Выключена"
    print(f"Опция 1: {option1_status}, Опция 2: {option2_status}")

# Создание главного окна
root = tk.Tk()
root.title("Приложение с чекбоксами")

# Переменные для хранения состояния чекбоксов
var1 = tk.IntVar()
var2 = tk.IntVar()

def status_getter():
    if (var1.get() == 1 and var2.get() ==0):
        print(f"Опция 1: Включена", "Опция 2: Выключена")
    elif (var1.get() == 1 and var2.get() ==1):
        print(f"Опция 1: Включена", "Опция 2: Включена")
    elif (var1.get() == 0 and var2.get() ==1):
        print(f"Опция 1: Выключена", "Опция 2: Включена")   
    elif (var1.get() == 0 and var2.get() ==0):
        print(f"Опция 1: Выключена", "Опция 2: Выключена") 
# Создание чекбоксов
check1 = tk.Checkbutton(root,text="Опция 1",variable=var1,command=status_getter)
check2 = tk.Checkbutton(root,text="Опция 2",variable=var2,command=status_getter)

# Размещение чекбоксов на окне
check1.pack()
check2.pack()

# Запуск главного цикла приложения
root.mainloop()