def absolute(lst):
    abs_lst = list()
    for element in lst:
        abs_lst.append(abs(float(element)))
    print(abs_lst)


lst_items = input().split(' ')
absolute(lst_items)
