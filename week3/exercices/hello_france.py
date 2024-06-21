items = input().split('|')
budget = float(input())
items_price = list()
clothes_max = 50.00
shoes_max = 35.00
accessories_max = 20.50
profits = 0
price_bought = 0
items_sold = list()

for item in items:
    items_price.append(item.split('->'))


for item in items_price:
    if ((item[0] == 'Clothes' and float(item[1]) <= clothes_max
        or item[0] == 'Shoes' and float(item[1]) <= shoes_max
        or item[0] == 'Accessories' and float(item[1]) <= accessories_max)
            and float(item[1]) <= budget):
        budget -= float(item[1])
        price_bought += float(item[1])
        price = float(item[1]) + float(item[1]) * 0.4
        items_sold.append(price)
        profits += price

for item in items_sold:
    print(f'{item:.2f}', end=' ')
print(f'\nProfit: {profits - price_bought:.2f}')

if budget + profits >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
