def print_products(prod: dict):
    for i, j in prod.items():
        print(f"{i} -> {j['price'] * j['quantity']:.2f}")


products = {}

while True:
    command = input()
    if command == 'buy':
        break

    product, price, quantity = command.split()
    if product in products.keys():
        products[product]['price'] = float(price)
        products[product]['quantity'] += int(quantity)
    else:
        products[product] = {}
        products[product]['price'] = float(price)
        products[product]['quantity'] = int(quantity)

print_products(products)
