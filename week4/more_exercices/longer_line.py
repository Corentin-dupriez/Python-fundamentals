from math import sqrt, floor


def calc_longer_line():
    point1_x, point1_y = float(input()), float(input())
    point2_x, point2_y = float(input()), float(input())
    point3_x, point3_y = float(input()), float(input())
    point4_x, point4_y = float(input()), float(input())

    dist_1 = sqrt(point1_x ** 2 + point1_y ** 2)
    dist_2 = sqrt(point2_x ** 2 + point2_y ** 2)
    dist_3 = sqrt(point3_x ** 2 + point3_y ** 2)
    dist_4 = sqrt(point4_x ** 2 + point4_y ** 2)

    len_1_2 = sqrt((point1_x - point2_x) ** 2 + (point1_y - point2_y) ** 2)
    len_3_4 = sqrt((point3_x - point4_x) ** 2 + (point3_y - point4_y) ** 2)

    if len_1_2 >= len_3_4:
        if dist_1 <= dist_2:
            print(f'({floor(point1_x)}, {floor(point1_y)})({floor(point2_x)}, {floor(point2_y)})')
        elif dist_1 > dist_2:
            print(f'({floor(point2_x)}, {floor(point2_y)})({floor(point1_x)}, {floor(point1_y)})')
    elif len_1_2 < len_3_4:
        if dist_3 <= dist_4:
            print(f'({floor(point3_x)}, {floor(point3_y)})({floor(point4_x)}, {floor(point4_y)})')
        else:
            print(f'({floor(point4_x)}, {floor(point4_y)})({floor(point3_x)}, {floor(point3_y)})')


calc_longer_line()
