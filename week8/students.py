def add_student_in_list(student_nb, student_name):
    if student_nb not in students_list:
        students_list[student_nb] = student_name


def add_student_to_course(course, student_nb):
    if course in courses_list:
        courses_list[course].append(student_nb)
    else:
        courses_list[course] = [student_nb]


def show_students_in_course(course):
    course = ' '.join(course.split('_'))
    for student in courses_list[course]:
        print(f'{students_list[student]} - {student}')


students_list = {}
courses_list = {}

while True:
    command = input().split(':')
    if len(command) == 1:
        break
    name = command[0]
    student_number = command[1]
    course_name = command[2]
    add_student_in_list(student_number, name)
    add_student_to_course(course_name, student_number)

show_students_in_course(command[0])
