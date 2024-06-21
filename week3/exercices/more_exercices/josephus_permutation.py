people = input().split(' ')
k = int(input())
k_people = []
length = len(people)
person = 0
counter = 0

while len(people) > 0:
    counter += 1
    if counter % k == 0:
        k_people.append(people.pop(person))
    else:
        person += 1
    if person >= len(people):
        person = 0

for k_person in k_people:
    if k_people.index(k_person) == 0:
        print(f'[{k_person},', end='')
    elif k_people.index(k_person) == len(k_people)-1:
        print(f'{k_person}]', end='')
    else:
        print(f'{k_person},', end='')
