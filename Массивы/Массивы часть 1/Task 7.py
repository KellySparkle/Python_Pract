# Дано: информация о студенте вуза содержит следующие элементы: 
# а) фамилия, имя; 
# б) шифр группы; 
# в) массив оценок по каждой дисциплине за семестр (от 2 до 5). 
# Информация о студенте является элементом массива М[ ]. 
# Требуется определить фамилии студентов, которые будут включены в приказ на отчисление по результатам сессии 
# (условие – по трем или более дисциплинам каждая оценка — двойка).

class Student:
    def __init__(self, surname, name, group_code, grades):
        self.surname = surname
        self.name = name
        self.group_code = group_code
        self.grades = grades

def find_students_for_expulsion(students):
    students_for_expulsion = []
    
    for student in students:
        twos_count = sum(1 for grade in student.grades if grade == 2)
        
        if twos_count >= 3:
            students_for_expulsion.append(student.surname)
    
    return students_for_expulsion

# Пример использования
students = [
    Student("Иванов", "Иван", "Г-101", [2, 2, 2, 3, 4]),
    Student("Петров", "Петр", "Г-102", [3, 4, 5, 5, 5]),
    Student("Сидоров", "Сидор", "Г-103", [2, 2, 2, 2, 3]),
    Student("Кузнецов", "Кузьма", "Г-104", [2, 3, 4, 5, 5]),
]

# Вывести фамилии студентов, подлежащих отчислению
expulsion_surnames = find_students_for_expulsion(students)
print("Фамилии студентов, подлежащих отчислению:", expulsion_surnames)
