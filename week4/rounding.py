def round_list(lst):
    rounded_list = list()
    for element in lst:
        rounded_list.append(round(float(element)))
    print(rounded_list)


round_list(input().split(' '))
