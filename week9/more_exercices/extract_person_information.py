def find_name(presentation_string, info):
    info_to_return = ''
    start_recording = False
    for char in presentation_string:
        if (info == 'name' and char == '@') \
                or (info == 'age' and char == '#'):
            start_recording = True
        elif (info == 'name' and char == '|') \
                or (info == 'age' and char == '*'):
            return info_to_return
        elif start_recording:
            info_to_return += char


def present_person(presentation_string):
    person_name = find_name(presentation_string, 'name')
    person_age = find_name(presentation_string, 'age')
    return f'{person_name} is {person_age} years old.'


nb_people = int(input())
for person in range(nb_people):
    presentation = input()
    print(present_person(presentation))
