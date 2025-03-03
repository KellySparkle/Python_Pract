# Напишите программу, в которой в цикле while пользователь вводит произвольное количество чисел, 
# а программа вычисляет их сумму. После каждого ввода спрашивайте пользователя, 
# закончил ли он ввод чисел. Если пользователь ввел "y" или "Y", то ввод чисел завершается, 
# после чего программа должна вывести сумму всех введенных чисел и их среднее арифметическое.

def calculate_sum_and_average():
    """
    Вычисляет сумму и среднее арифметическое введенных чисел.
    """
    total_sum = 0
    count = 0
    
    while True:
        try:
            number = float(input("Введите число: "))
            total_sum += number
            count += 1
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")
            continue
        
        finish = input("Закончить ввод? (y/n): ")
        
        if finish.lower() == 'y':
            break
    
    if count == 0:
        print("Вы не ввели ни одного числа.")
    else:
        average = total_sum / count
        print(f"Сумма введенных чисел: {total_sum}")
        print(f"Среднее арифметическое: {average}")

def main():
    while True:
        calculate_sum_and_average()
        
        cont = input("Продолжить ввод? (y/n): ")
        if cont.lower() != 'y':
            print("Программа завершена.")
            break

if __name__ == "__main__":
    main()
