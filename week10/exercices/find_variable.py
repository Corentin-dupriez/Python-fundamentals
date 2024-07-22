import re

pattern = r'\b_{1}([a-zA-Z]+)\b'

text = input()

matches = re.findall(pattern, text)

print(','.join(matches))
