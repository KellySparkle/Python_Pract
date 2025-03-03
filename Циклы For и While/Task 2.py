# Необходимо суммировать все нечётные целые числа в диапазоне, который введёт пользователь с клавиатуры.

def sum_odd_numbers(start, end):
   
   
    """
    Суммирует все нечётные целые числа в диапазоне от start до end включительно.
    
    :param start: Начало диапазона
    :param end: Конец диапазона
    :return: Сумма нечётных чисел
    """
    return sum(i for i in range(start, end + 1) if i % 2 != 0)

def main():
    while True:
        try:
            start = int(input("Введите начало диапазона: "))
            end = int(input("Введите конец диапазона: "))
            
            if start > end:
                print("Начало диапазона должно быть меньше или равно концу.")
                continue
            
            sum_of_odd = sum_odd_numbers(start, end)
            print(f"Сумма нечётных чисел в диапазоне от {start} до {end} равна: {sum_of_odd}")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")
        
        cont = input("Продолжить? (y/n): ")
        if cont.lower() != 'y':
            print("Программа завершена.")
            break

if __name__ == "__main__":
    main()
