def print_squares_of_odd_numbers(limit):
    """
    Выводит квадраты нечётных целых чисел от 1 до заданного предела.
    
    :param limit: Верхний предел
    """
    for i in range(1, limit + 1):
        if i % 2 != 0:
            square = i * i + 1  
            print(f"Квадрат числа {i} равен {square}")

def main():
    while True:
        try:
            limit = int(input("Введите верхний предел: "))
            if limit < 1:
                print("Предел должен быть целым положительным числом.")
                continue
            
            print_squares_of_odd_numbers(limit)
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")
        
        cont = input("Продолжить? (y/n): ")
        if cont.lower() != 'y':
            print("Программа завершена.")
            break

if __name__ == "__main__":
    main()
