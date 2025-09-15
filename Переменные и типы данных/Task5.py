# Дано число секунд. Переведи его в минуты и часы.
seconds = int(input("Введите количество секунд: "))
minutes = seconds / 60
hours = seconds / 3600
print("Минуты:", minutes, "Часы:", hours)