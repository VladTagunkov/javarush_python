from datetime import datetime, timedelta

def round_time_to_nearest_half_hour(time_str):
    # Преобразуем строку во временной объект
    time_ = datetime.strptime(time_str,"%H:%M")
    
    # Получаем количество минут и округляем до ближайших 30 минут
    mins = time_.minute
    if mins > 14 and mins < 45:
        add_mins = 30 - mins
        time_ += timedelta(minutes=add_mins)
    elif mins < 15:
        #add_mins = 30 - mins
        time_ -= timedelta(minutes=mins)
    elif mins > 44:
        add_mins = 60 - mins
        time_ += timedelta(minutes=add_mins)
        
    

    return time_

def process_time_stamps(time_stamps):
    res = []
    for elem in time_stamps:
        new_ts = round_time_to_nearest_half_hour(elem)
        res.append(new_ts.strftime("%H:%M"))
    return res


# Пример использования:
time_stamps = ["14:07", "15:29", "16:45", "22:59", "23:15"]
rounded_times = process_time_stamps(time_stamps)
print(rounded_times)