# Использование ThreadLocal

# Напишите программу, которая использует класс ThreadLocal для хранения данных, уникальных для каждого потока.

# Напишите тут ваш код
import threading

local_dat = threading.local()

def proc_data():
    local_dat.value = threading.current_thread().name
    print(f"value in {threading.current_thread().name}:{local_dat.value}")
    
thr = []
for i in range(5):
    t = threading.Thread(target=proc_data)
    thr.append(t)
    t.start()
    
for t in thr:
    t.join()