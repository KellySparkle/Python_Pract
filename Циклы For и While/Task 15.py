# Создайте цикл Do..while с 5 итерациями (повторениями), который выводит значения счетчика цикла.

def display_counter():
    counter = 1
    while True:
        print(f"Значение счетчика: {counter}")
        counter += 1
        if counter > 5:
            break

# Выполнить цикл
display_counter()

