grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
def calculate_average(grades):
    total = sum(grades)
    return total / len(grades) if grades else 0
averages = {student: calculate_average(grade) for student, grade in zip(students, grades)}
print(averages)
