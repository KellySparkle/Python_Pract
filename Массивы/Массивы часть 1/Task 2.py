# Задан массив действительных чисел размерности 10х10. Найти суммы элементов каждой строки, 
# произведения элементов каждого столбца, и максимальный элемент главной диагонали 
# (подсказка: все элементы, для которых номер строки совпадает с номером столбца).

import numpy as np

def calculate_array_properties():
    # Создать массив 10х10 с случайными значениями
    array = np.random.rand(10, 10)
    
    # Вывести массив
    print("Исходный массив:")
    print(array)
    
    # Рассчитать суммы элементов каждой строки
    row_sums = np.sum(array, axis=1)
    print("\nСуммы элементов каждой строки:")
    print(row_sums)
    
    # Рассчитать произведения элементов каждого столбца
    column_products = np.prod(array, axis=0)
    print("\nПроизведения элементов каждого столбца:")
    print(column_products)
    
    # Найти максимальный элемент главной диагонали
    diagonal_elements = np.diag(array)
    max_diagonal_element = np.max(diagonal_elements)
    print(f"\nМаксимальный элемент главной диагонали: {max_diagonal_element}")

# Выполнить функцию
calculate_array_properties()
