capacity = 255
total_liters = 0

pours = int(input())

for pour in range(pours):
    liters = int(input())
    if total_liters + liters <= capacity:
        total_liters += liters
    else:
        print('Insufficient capacity!')

print(total_liters)
