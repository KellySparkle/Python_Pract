# В некотором году (назовем его условно первым) на участке в 100 гектаров средняя урожайность ячменя составила 20 центнеров с гектара. 
# После этого каждый год площадь участка увеличивалась на 5%, а средняя урожайность на 2%. Определить: 
# а) в каком году урожайность превысит 22 центнера с гектара; 
# б) в каком году площадь участка станет больше 120 гектаров; 
# в) в каком году общий урожай, собранный за все время, начиная с первого года, превысит 800 центнеров.

def calculate_yearly_data(initial_area, initial_yield, area_growth, yield_growth):
    years = []
    total_yield = 0
    current_area = initial_area
    current_yield = initial_yield
    
    for year in range(1, 100):  # Достаточно большое количество лет
        # Рассчитать урожай за текущий год
        yearly_yield = current_area * current_yield
        
        # Добавить в список данных за год
        years.append({
            'year': year,
            'area': current_area,
            'yield_per_ha': current_yield,
            'total_yield': yearly_yield
        })
        
        # Обновить общий урожай
        total_yield += yearly_yield
        
        # Обновить площадь и урожайность на следующий год
        current_area *= (1 + area_growth)
        current_yield *= (1 + yield_growth)
        
        # Проверить условия
        if current_yield > 22 and not hasattr(calculate_yearly_data, 'yield_exceeded'):
            calculate_yearly_data.yield_exceeded = year
        if current_area > 120 and not hasattr(calculate_yearly_data, 'area_exceeded'):
            calculate_yearly_data.area_exceeded = year
        if total_yield > 800 and not hasattr(calculate_yearly_data, 'total_yield_exceeded'):
            calculate_yearly_data.total_yield_exceeded = year
        
        # Если все условия выполнены, можно остановиться
        if hasattr(calculate_yearly_data, 'yield_exceeded') and hasattr(calculate_yearly_data, 'area_exceeded') and hasattr(calculate_yearly_data, 'total_yield_exceeded'):
            break
    
    return years

# Начальные условия
initial_area = 100  # гектаров
initial_yield = 20  # центнеров с гектара
area_growth = 0.05  # 5%
yield_growth = 0.02  # 2%

# Рассчитать данные за годы
years_data = calculate_yearly_data(initial_area, initial_yield, area_growth, yield_growth)

# Вывод результатов
print(f"а) Урожайность превысит 22 центнера с гектара в {getattr(calculate_yearly_data, 'yield_exceeded', 'не определено')} году.")
print(f"б) Площадь участка станет больше 120 гектаров в {getattr(calculate_yearly_data, 'area_exceeded', 'не определено')} году.")
print(f"в) Общий урожай превысит 800 центнеров в {getattr(calculate_yearly_data, 'total_yield_exceeded', 'не определено')} году.")
