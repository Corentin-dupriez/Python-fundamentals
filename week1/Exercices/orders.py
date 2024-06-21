n = int(input())
total = 0

for _ in range(n):
    price = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if ((price < 0.01 or price > 100.00) or (days not in range(1, 32)) or
            (capsules_per_day < 1 or capsules_per_day > 2000)):
        continue
    else:
        price_order = price * days * capsules_per_day
        print(f'The price for the coffee is: ${price_order:.2f}')
        total += price_order

print(f'Total: ${total:.2f}')
