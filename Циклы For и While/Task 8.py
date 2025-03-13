# Напишите программу, которая вводит натуральное число N и находит сумму всех натуральных чисел от 1 до N. 
# Входные данные: входная строка содержит единственное целое число N. 
# Выходные данные: программа должна вывести сумму натуральных чисел от 1 до введённого числа N

def sum_natural_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    total += 1  
    return total

# Ввод натурального числа N
n = int(input("Введите натуральное число N: "))

# Вывод суммы
print("Сумма натуральных чисел от 1 до", n, "равна:", sum_natural_numbers(n))

