from math import sqrt, floor


def find_center_point(x_1, y_1, x_2, y_2):
    dist1 = sqrt(x_1 ** 2 + y_1 ** 2)
    dist2 = sqrt(x_2 ** 2 + y_2 ** 2)
    if dist1 < dist2:
        print(f'({floor(x_1)}, {floor(y_1)})')
    else:
        print(f'({floor(x_2)}, {floor(y_2)})')


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

find_center_point(x1, y1, x2, y2)
