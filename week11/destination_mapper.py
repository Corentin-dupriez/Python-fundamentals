import re

pattern = r'(=|\/)([A-Z]{1}[A-Za-z]{2,})\1'

places = input()

places = re.findall(pattern, places)
valid_places = []
travel_points = 0

for place in places:
    destination = place[1]
    valid_places.append(destination)
    travel_points += len(destination)

print(f'Destinations: {", ".join(valid_places)}')
print(f'Travel Points: {travel_points}')
