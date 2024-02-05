from datetime import datetime, timedelta

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
    while current_time + visit_duration <= break_start_time:
        visit_end_time = current_time + visit_duration
        visit_grid.append((current_time.time(), visit_end_time.time()))
        current_time = visit_end_time

    # Добавляем перерыв
    break_end_time = break_start_time + break_duration
    visit_grid.append(("Break", break_start_time.time(), break_end_time.time()))
    current_time = break_end_time
    
    # Генерируем визиты после перерыва до конца дня
    while current_time + visit_duration <= end_time:
        visit_end_time = current_time + visit_duration
        visit_grid.append((current_time.time(), visit_end_time.time()))
        current_time = visit_end_time
    
    return visit_grid

# Пример использования
start_time = '09:00'
end_time = '18:00'
visit_duration = timedelta(minutes=40)
break_start_time = '12:00'
break_duration = timedelta(hours=1)

visit_schedule = generate_visit_schedule(start_time, end_time, visit_duration, break_start_time, break_duration)

for visit in visit_schedule:
    print(visit)

