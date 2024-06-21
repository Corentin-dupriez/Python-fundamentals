group_size = int(input())
days = int(input())
profit = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    profit += 50
    profit -= 2 * group_size
    if day % 3 == 0:
        profit -= 3 * group_size
    if day % 5 == 0:
        profit += 20 * group_size
        if day % 3 == 0:
            profit -= 2 * group_size

profit_per_person = profit // group_size
print(f'{group_size} companions received {profit_per_person} coins each.')
