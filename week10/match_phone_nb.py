import re

numbers = input()

regex = r"\+359-2-[0-9]{3}-[0-9]{4}\b|\+359 2 [0-9]{3} [0-9]{4}\b"

x = re.findall(regex, numbers)

print(', '.join(x))
