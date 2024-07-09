def add_student_and_grade(student: str, grade: float):
    if students_and_grades.get(student):
        students_and_grades[student].append(grade)
    else:
        students_and_grades[student] = [grade]


def print_students(students: dict):
    for student in students.keys():
        if sum(students[student]) / len(students[student]) >= 4.5:
            print(f'{student} -> {sum(students[student]) / len(students[student]):.2f}')


nb_of_rows = int(input())

students_and_grades = dict()

for i in range(nb_of_rows):
    student_name = input()
    student_grade = float(input())
    add_student_and_grade(student_name, student_grade)

print_students(students_and_grades)
