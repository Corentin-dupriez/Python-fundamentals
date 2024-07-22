import re

pattern = r'>>(\w+)<<(\d+\.?\d+)!(\d+)'
bought_furniture = []
total_spent = 0

while True:
    command = input()
    if command == 'Purchase':
        break
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_spent += float(price) * int(quantity)

print('Bought furniture:')
print(*bought_furniture, sep='\n')
print(f'Total money spend: {total_spent:.2f}')
