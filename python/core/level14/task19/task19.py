# Использование многопроцессорности

# Напишите программу, которая создает 4 параллельных процесса.
# Каждый процесс должен печатать свое имя и текущий идентификатор процесса.
# Используйте модуль multiprocessing.

# Напишите тут ваш код
import multiprocessing 

def work(i):
    id_ = multiprocessing.current_process().pid
    name_ = multiprocessing.current_process().name
    print(f"Worker{i}:{id_} and {name_}")
    
def main():
    process = []
    for i in range(4):
        p = multiprocessing.Process(target = work, args=(i))
        process.append(p)
        p.start()
        
    for p in process:
        p.join()
        
        
main()