# Сформируйте массив целых чисел по алгоритму Фибоначчи: 
# 1-й и 2-й элемент равны 1, а каждый последующий равен сумме двух предыдущих, 
# т.е.: 1, 1, 2, 3, 5, 8, … . Найдите сумму и произведение его N членов.

def fibonacci_sequence(n):
    # Инициализировать последовательность Фибоначчи
    sequence = [1, 1]
    
    # Генерировать последовательность до N членов
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    
    return sequence

def calculate_sum_and_product(sequence):
    # Рассчитать сумму членов
    total_sum = sum(sequence)
    
    # Рассчитать произведение членов
    total_product = 1
    for num in sequence:
        total_product *= num
    
    return total_sum, total_product

# Запросить количество членов N
n = int(input("Введите количество членов N: "))

# Сформировать последовательность Фибоначчи
fib_sequence = fibonacci_sequence(n)

# Вывести последовательность
print("Последовательность Фибоначчи:")
print(fib_sequence)

# Рассчитать и вывести сумму и произведение
total_sum, total_product = calculate_sum_and_product(fib_sequence)
print(f"\nСумма {n} членов: {total_sum}")
print(f"Произведение {n} членов: {total_product}")
