def calc_order():
    product = input()
    quantity = int(input())
    if product == 'water':
        price = quantity * 1.00
    elif product == 'coffee':
        price = quantity * 1.5
    elif product == 'coke':
        price = quantity * 1.4
    elif product == 'snacks':
        price = quantity * 2.00
    print(f'{price:.2f}')


calc_order()
