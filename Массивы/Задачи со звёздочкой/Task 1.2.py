# Создать трехмерный массив на 5х5х5 целых чисел и заполнить его случайными значениями в диапазоне от 0 до 1000. 
# Найти элементы массива, значения которых кратны 6, и вывести их в консоль в порядке возрастания.

import random

def create_and_find_multiples():
    # Создать трехмерный массив
    array = [[[random.randint(0, 1000) for _ in range(5)] for _ in range(5)] for _ in range(5)]
    
    # Вывести массив
    print("\nСгенерированный массив:")
    for i, plane in enumerate(array):
        print(f"Плоскость {i+1}:")
        for row in plane:
            print(row)
    
    # Найти элементы, кратные 6
    multiples_of_six = [element for plane in array for row in plane for element in row if element % 6 == 0]
    
    # Вывести элементы, кратные 6, в порядке возрастания
    if multiples_of_six:
        print(f"\nЭлементы, кратные 6, в порядке возрастания: {sorted(multiples_of_six)}")
    else:
        print("\nЭлементов, кратных 6, не найдено.")

# Выполнить функцию
create_and_find_multiples()
