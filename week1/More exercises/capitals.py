word = str(input())
capital_places = []

for i in range(0, len(word)):
    if word[i].isupper():
        capital_places.append(i)

print(capital_places)
