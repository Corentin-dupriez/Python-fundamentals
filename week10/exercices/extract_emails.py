import re

pattern = r'\s([a-z0-9]+[\w\.\-]?[a-z]+@[a-z\-]+(\.[a-z]+)+)\b'

str_to_search = input()

matches = re.findall(pattern, str_to_search)

for match in matches:
    print(match[0])
