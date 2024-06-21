ornaments = {'price': 2, 'points': 5}
skirt = {'price': 5, 'points': 3}
garland = {'price': 3, 'points': 10}
lights = {'price': 15, 'points': 17}

spirit = 0
budget = 0

quantity = int(input())
days = int(input())

for i in range(1, days+1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        spirit += ornaments['points']
        budget += ornaments['price'] * quantity
    if i % 3 == 0:
        spirit += skirt['points'] + garland['points']
        budget += (skirt['price'] + garland['price']) * quantity
    if i % 5 == 0:
        spirit += lights['points']
        budget += lights['price'] * quantity
        if i % 3 == 0:
            spirit += 30
    if i % 10 == 0:
        spirit -= 20
        budget += skirt['price'] + lights['price'] + garland['price']
    if days % 10 == 0 and i == days:
        spirit -= 30

print(f'Total cost: {budget}')
print(f'Total spirit: {spirit}')
