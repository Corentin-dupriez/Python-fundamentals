import re

str_to_search_in = input()
str_to_search_for = input()

pattern = fr'\b{str_to_search_for}\b'

matches = re.findall(pattern, str_to_search_in, re.IGNORECASE)

print(len(matches))
