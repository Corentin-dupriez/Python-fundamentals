number = float(input())

if number == 0: 
    print('zero')
else: 
    if abs(number) < 1: 
        print('small', end=' ')
    elif abs(number) > 1000000:
        print('large', end=' ')
    if number < 0:
        print('negative')
    else: 
        print('positive')