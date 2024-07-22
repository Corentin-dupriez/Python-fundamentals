import re

participants = input().split(', ')
results = dict()
for participant in participants:
    results[participant] = 0
pattern = r'(?P<Letters>[a-zA-Z]+)|(?P<Digits>[0-9])'

while True:
    name = ''
    km = 0
    command = input()
    if command == 'end of race':
        break
    matches = re.findall(pattern, command)
    for match in matches:
        name += match[0]
        if match[1]:
            km += int(match[1])
    if name in results:
        results[name] += km

ordered_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

print(f'1st place: {ordered_results[0][0]}')
print(f'2nd place: {ordered_results[1][0]}')
print(f'3rd place: {ordered_results[2][0]}')
