# Пользователь вводит длину, ширину и высоту прямоугольного параллелепипеда. Найди его объём и площадь поверхности.

length = float(input("Введите длину: "))
width = float(input("Введите ширину: "))
height = float(input("Введите высоту: "))

volume = length * width * height
surface_area = 2 * (length * width + length * height + width * height)

print("Объем:", volume)
print("Площадь поверхности:", surface_area)
