import tkinter as tk

# Глобальные переменные для отслеживания времени и состояния таймера
time_elapsed = 0
running = False

# Функция для обновления таймера
def update_timer():
    if running:
        global time_elapsed
        time_elapsed += 1
        label.config(text=f"Прошло секунд: {time_elapsed}")
        root.after(1000, update_timer)


# Функция для запуска таймера
def start_timer():
    global time_elapsed
    global running
    if not running:
        running = True
        update_timer()

# Функция для остановки таймера
def stop_timer():
    global running
    running = False


# Функция для сброса таймера
def reset_timer():
    global time_elapsed
    time_elapsed = 0 
    stop_timer()


# Создаем главное окно
root = tk.Tk()
root.title("Таймер")

# Метка для отображения времени
label = tk.Label(root, text="0", font=("Helvetica", 48))
label.pack()

# Кнопка Старт
start_button = tk.Button(root, text="Старт", command=start_timer)
start_button.pack(side=tk.LEFT)

# Кнопка Стоп
stop_button = tk.Button(root, text="Стоп", command=stop_timer)
stop_button.pack(side=tk.LEFT)

# Кнопка Сброс
reset_button = tk.Button(root, text="Сброс", command=reset_timer)
reset_button.pack(side=tk.LEFT)

# Запуск главного цикла приложения
root.mainloop()