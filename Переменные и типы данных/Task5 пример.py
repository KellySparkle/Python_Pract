#Пользователь вводит количество минут. Переведи это значение в часы и дни.

minutes = int(input("Введите количество минут: "))
hours = minutes / 60
days = minutes / (60 * 24)
print("Часы:", hours)
print("Дни:", days)