# Известно количество очков, набранных каждой из 20-ти команд-участниц первенства по футболу. 
# Перечень очков дан в порядке убывания (ни одна пара команд не набрала одинаковое количество очков). 
# Определить, какое место заняла команда, набравшая N очков (естественно, что значение N имеется в перечне). 
# Условный оператор не использовать

def find_place(points, n):
    for i, point in enumerate(points):
        if point == n:
            return i + 1

# Ввод очков для 20 команд
points = list(map(int, input("Введите очки для 20 команд через пробел: ").split()))

# Ввод количества очков N
n = int(input("Введите количество очков N: "))

# Вывод места команды
print("Место команды с", n, "очками:", find_place(points, n))

