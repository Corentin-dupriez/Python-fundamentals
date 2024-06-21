def mutlipl_sign(n1, n2, n3):
    if n3 < 0 < n1 * n2 or n1 * n2 < 0 < n3:
        print('negative')
    elif n3 == 0 or n1 * n2 == 0:
        print('zero')
    else:
        print('positive')


number1 = int(input())
number2 = int(input())
number3 = int(input())

mutlipl_sign(number1, number2, number3)
