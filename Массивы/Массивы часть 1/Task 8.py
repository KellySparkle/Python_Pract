# Известны (вводятся с клавиатуры) размеры 10 треугольников (задаются три стороны). 
# Напишите функцию, вычисляющую площадь треугольника по формуле Герона и с ее помощью определите номер треугольника с наибольшей площадью.

import math

def calculate_triangle_area(a, b, c):
    # Вычислить полупериметр
    s = (a + b + c) / 2
    
    # Вычислить площадь по формуле Герона
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return area

def find_largest_triangle(triangles):
    max_area = 0
    max_triangle_index = 0
    
    for i, triangle in enumerate(triangles):
        a, b, c = triangle
        
        # Проверить, можно ли образовать треугольник
        if a + b > c and a + c > b and b + c > a:
            area = calculate_triangle_area(a, b, c)
            
            if area > max_area:
                max_area = area
                max_triangle_index = i + 1  # Номер треугольника
        else:
            print(f"Треугольник {i+1} не может быть образован.")
    
    return max_triangle_index, max_area

# Ввод размеров треугольников
triangles = []
for i in range(10):
    while True:
        try:
            a, b, c = map(float, input(f"Введите размеры треугольника {i+1} (три стороны через пробел): ").split())
            triangles.append((a, b, c))
            break
        except ValueError:
            print("Пожалуйста, введите три числа через пробел.")

# Найти треугольник с наибольшей площадью
max_triangle_index, max_area = find_largest_triangle(triangles)

if max_area > 0:
    print(f"\nТреугольник с наибольшей площадью — это треугольник {max_triangle_index} с площадью {max_area:.2f}.")
else:
    print("\nНи один из треугольников не может быть образован.")
