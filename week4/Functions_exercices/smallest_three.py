def smallest_three():
    nb_lst = list()
    for _ in range(3):
        number = int(input())
        nb_lst.append(number)
    print(min(nb_lst))


smallest_three()