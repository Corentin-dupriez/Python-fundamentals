import re

pattern = r'(w{3}.[a-zA-Z0-9\-]+(\.[a-z]+)+)'

while True:
    text_to_search_in = input()
    if not text_to_search_in:
        break
    matches = re.search(pattern, text_to_search_in)
    if matches:
        print(matches[0], sep='\n')
