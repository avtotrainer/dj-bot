from datetime import datetime, timedelta

def sub_visit_shedule(start_time, end_time, visit_duration):
    sub_grid = []
    while start_time + visit_duration <= end_time:
        sub_grid.append(start_time)
        start_time = start_time + visit_duration
    return sub_grid

def generate_visit_schedule(start_time, end_time, visit_duration, break_start_time, break_duration):
    # Преобразуем строки времени в объекты datetime для удобства работы
    start_time = datetime.strptime(start_time, '%H:%M')
    end_time = datetime.strptime(end_time, '%H:%M')
    break_start_time = datetime.strptime(break_start_time, '%H:%M')
    
    # Инициализируем текущее время начала дня
    current_time = start_time
    
    # Сетка визитов
    visit_grid = []

    # Генерируем визиты до начала перерыва
    visit_grid.append(sub_visit_shedule(current_time,break_start_time, visit_duration))

    # Назначаем дополнительный визит с учетом продолжительности
    current_time = break_start_time + break_duration

    visit_grid.append(sub_visit_shedule(current_time,end_time, visit_duration))
   
    
    return visit_grid

# Пример использования
start_time = '09:00'
print(datetime.strptime(start_time, '%H:%M'))
end_time = '18:00'
visit_duration = timedelta(minutes=45)
break_start_time = '12:00'
break_duration = timedelta(hours=1)

visit_schedule = generate_visit_schedule(start_time, end_time, visit_duration, break_start_time, break_duration)

"""
formatted_schedules = []
for schedule in visit_schedule:
    formatted_times = [dt.strftime("%H:%M") for dt in schedule]
    formatted_schedules.append(formatted_times)

print(formatted_schedules)
"""
