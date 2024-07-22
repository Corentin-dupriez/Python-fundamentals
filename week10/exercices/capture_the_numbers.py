import re
pattern = r'\d+'
all_matches = []

while True:
    command = input()
    if not command:
        break
    matches = re.findall(pattern, command)
    if matches:
        all_matches.extend(matches)


print(' '.join(all_matches))
