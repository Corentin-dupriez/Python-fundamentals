sequence = input().split()
elements_and_occurrences = {}

for element in sequence:
    if element.lower() in elements_and_occurrences:
        elements_and_occurrences[element.lower()] += 1
    else:
        elements_and_occurrences[element.lower()] = 1

for item in elements_and_occurrences:
    if elements_and_occurrences[item] % 2 != 0:
        print(item, end=' ')
        