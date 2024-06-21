def sum_nb(int1, int2):
    result = int1 + int2
    return result


def subtract(int3, int4):
    result = int3 - int4
    return result


def add_and_subtract():
    num = list()
    for _ in range(3):
        num_to_add = int(input())
        num.append(num_to_add)
    result_add = sum_nb(num[0], num[1])
    result_sub = subtract(result_add, num[2])
    print(result_sub)


add_and_subtract()
