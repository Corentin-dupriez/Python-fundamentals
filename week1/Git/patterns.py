import math
def pattern_1():
    size = int(input())
    for i in range(1, size+1):
        print('*' * i)


def pattern_2():
    size = int(input())
    for i in range(1, size+1):
        if i == 1 or i == size:
            print('*' * size)
        else:
            print('*' + ' ' * (size-2) + '*')


def pattern_3():
    size = int(input())
    for i in range(1, size+1, 2):
        print(' ' * round((size - i) / 2),  '*' * i)
    for i in range(size - 2, 0, -2):
        print(' ' * round((size - i) / 2), '*' * i)


def pattern_4():
    size = int(input())
    for i in range(size, 0, -1):
        print('*' * i)


def pattern_6(size):
    for i in range(1, size + 1):
        for j in range(size - 1):
            print(' ', end='')
        for k in range(1, 2 * i):
            print('*', end='')


pattern_6(4)
