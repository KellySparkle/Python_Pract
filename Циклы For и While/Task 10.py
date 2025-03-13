# Дано натуральное число. 
# а) Получить все его делители. 
# б) Найти сумму его делителей. 
# в) Найти сумму его четных делителей. 
# г) Определить количество его делителей. 
# д) Определить количество его нечетных делителей. 
# е) Определить количество его делителей. Сколько из них четных? 
# ж) Найти количество его делителей, больших d.

def find_divisors(n):
    divisors = []
    for i in range(1, n):  
        if n % i == 0:
            divisors.append(i)
    return divisors

def sum_of_divisors(divisors):
    return sum(divisors)

def sum_of_even_divisors(divisors):
    return sum(d for d in divisors if d % 2 == 0)

def count_divisors(divisors):
    return len(divisors)

def count_odd_divisors(divisors):
    return sum(1 for d in divisors if d % 2 != 0)

def count_even_divisors(divisors):
    return sum(1 for d in divisors if d % 2 == 0)

def count_divisors_greater_than_d(divisors, d):
    return sum(1 for divisor in divisors if divisor > d)
