bakery = {}
nb_products = 0
sum_quantity = 0

while True:
    command = input().split(': ')

    if command[0] == 'statistics':
        break

    if command[0] in bakery:
        bakery[command[0]] += int(command[1])
    else:
        bakery[command[0]] = int(command[1])

print('Products in stock:')
for product in bakery:
    print(f'- {product}: {bakery[product]}')
    nb_products += 1
    sum_quantity += int(bakery[product])
print(f'Total Products: {nb_products}\nTotal Quantity: {sum_quantity}')
