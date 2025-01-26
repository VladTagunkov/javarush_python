import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_graph():
    # Исходные данные
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    
    # Создаем новый график
    fig = plt.figure(figsize=(5,4),dpi=100)
    plot = fig.add_subplot(111)
    plot.plot(x,y)
    
    # Задаем заголовки
    plot.set_title("Example Graph")
    plot.set_xlabel('x')
    plot.set_ylabel('y')

    # Встраиваем график в окно Tkinter
    canvas = FigureCanvasTkAgg(fig,master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()


# Создаем основное окно приложения
window = tk.Tk()
window.title("Построение графика")

# Создаем и размещаем кнопку для построения графика
plot_button = ttk.Button(window, text="Построить график", command=plot_graph)
plot_button.pack()

# Запускаем главный цикл обработки событий
window.mainloop()