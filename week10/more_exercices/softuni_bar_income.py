import re

pattern = r'%(?P<Name>[A-Z]{1}[a-z]+)%\w*<(?P<Product>\w+)>\w*\|(?P<Quantity>[0-9]+)\|[A-Z]*(?P<Price>[0-9]+\.?[0-9]+)\$'
profit = 0


while True:
    command = input()
    if command == 'end of shift':
        break
    matches = re.search(pattern, command)
    if matches:
        client_name, product, quantity, price = matches.groups()
        earned = int(quantity) * float(price)
        print(f'{client_name}: {product} - {earned:.2f}')
        profit += earned

print(f'Total income: {profit:.2f}')
