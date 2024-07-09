def add_student_to_course(course_name: str, student_name: str):
    if courses.get(course_name):
        courses[course_name].append(student_name)
    else:
        courses[course_name] = [student_name]


def print_course_attendees(courses_and_students: dict):
    for course_name in courses_and_students.keys():
        print(f'{course_name}: {len(courses_and_students[course_name])}')
        for student_name in courses_and_students[course_name]:
            print(f'-- {student_name}')


courses = dict()

while True:
    command = input()
    if command == 'end':
        break
    course, student = command.split(' : ')
    add_student_to_course(course, student)

print_course_attendees(courses)
