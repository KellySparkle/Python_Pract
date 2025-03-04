# Введите с клавиатуры строку произвольной длины и подсчитайте процент вхождения заданного символа в строку.

def calculate_symbol_percentage():
    # Запросить строку и символ у пользователя
    input_string = input("Введите строку: ")
    symbol = input("Введите символ: ")
    
    # Проверить, что символ — это один символ
    if len(symbol) != 1:
        print("Пожалуйста, введите один символ.")
        return
    
    # Подсчитать количество вхождений символа
    symbol_count = input_string.count(symbol)
    
    # Подсчитать процент вхождения символа
    if len(input_string) == 0:
        print("Строка пуста.")
    else:
        percentage = (symbol_count / len(input_string)) * 100
        
        # Вывести результат
        print(f"Процент вхождения символа '{symbol}' в строку: {percentage:.2f}%")

# Выполнить функцию
calculate_symbol_percentage()
