def add_student(student_name: str, language_name: str, mark: int):
    if student_name in exam_results.keys():
        if language_name in exam_results[student_name]:
            if exam_results[student_name][language_name] < int(mark):
                exam_results[student_name][language_name] = int(mark)
    else:
        exam_results[student_name] = {language_name: int(mark)}
    count_submission_in_language(language_name)


def ban_student(student_name: str):
    exam_results.pop(student_name)


def print_submissions():
    print('Submissions:')
    for l, nb_l in list_languages.items():
        print(f'{l} - {nb_l}')


def print_students(exam_result: dict):
    print('Results:')
    for student, info in exam_result.items():
        for langue, mark in info.items():
            print(f'{student} | {mark}')
    print_submissions()


def count_submission_in_language(lang: str):
    if list_languages.get(lang):
        list_languages[lang] += 1
    else:
        list_languages[lang] = 1


exam_results = {}
list_languages = {}

while True:
    command = input()
    if command == 'exam finished':
        break
    if 'banned' in command:
        username, action = command.split('-')
        ban_student(username)
    else:
        username, language, points = command.split('-')
        add_student(username, language, points)

print_students(exam_results)
