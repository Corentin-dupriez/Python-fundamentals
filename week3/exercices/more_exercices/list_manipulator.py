list_given = input().split(' ')

for element in range(len(list_given)):
    list_given[element] = int(list_given[element])


def exchange(index):
    global list_given
    if index >= len(list_given):
        print('Invalid index')
    elif index < 0:
        pass
    else:
        new_list = []
        removed = list_given[:index + 1]
        data = list_given[index + 1:]
        for _i in data:
            new_list.append(_i)
        for _i in removed:
            new_list.append(_i)
        list_given = new_list


def max_min(minmax, odd_even):
    global list_given
    _temp_list = []
    if minmax == 'max':
        if odd_even == 'odd':
            for _i in list_given:
                if int(_i) % 2 != 0:
                    _temp_list.append(_i)
            if _temp_list:
                _max_nb = max(_temp_list)
                _max_nb_index = [i for i, n in enumerate(list_given) if n == _max_nb][-1]
                print(_max_nb_index)
            else:
                print('No matches')
        elif odd_even == 'even':
            for _i in list_given:
                if int(_i) % 2 == 0:
                    _temp_list.append(_i)
            if _temp_list:
                _max_nb = max(_temp_list)
                _max_nb_index = [i for i, n in enumerate(list_given) if n == _max_nb][-1]
                print(_max_nb_index)
            else:
                print('No matches')
    elif minmax == 'min':
        if odd_even == 'odd':
            for _i in list_given:
                if int(_i) % 2 != 0:
                    _temp_list.append(_i)
            if _temp_list:
                _min_nb = min(_temp_list)
                _min_nb_index = [i for i, n in enumerate(list_given) if n == _min_nb][-1]
                print(_min_nb_index)
            else:
                print('No matches')
        elif odd_even == 'even':
            for i in list_given:
                if int(i) % 2 == 0:
                    _temp_list.append(i)
            if _temp_list:
                _min_nb = min(_temp_list)
                _min_nb_index = [i for i, n in enumerate(list_given) if n == _min_nb][-1]
                print(_min_nb_index)
            else:
                print('No matches')


def first_last_odd_even(position, index, oddeven):
    _temp_list = []
    global list_given
    if int(index) <= len(list_given):
        if oddeven == 'odd':
            for _i in list_given:
                if int(_i) % 2 != 0:
                    _temp_list.append(int(_i))
            if position == 'first':
                print(_temp_list[:int(index)])
            elif position == 'last':
                if len(_temp_list) >= int(index):
                    print(_temp_list[int(index) + 1:])
                else:
                    print(_temp_list)
        elif oddeven == 'even':
            for _i in list_given:
                if int(_i) % 2 == 0:
                    _temp_list.append(int(_i))
                    _temp_list = sorted(_temp_list)
            if position == 'first':
                print(_temp_list[:int(index)])
            elif position == 'last':
                print(_temp_list[int(index) + 1:])
    else:
        print('Invalid count')


while True:
    command = input().split(' ')
    if command[0] == 'exchange':
        exchange(int(command[1]))
    elif command[0] in ('max', 'min'):
        max_min(command[0], command[1])
    elif command[0] in ('first', 'last'):
        first_last_odd_even(command[0], command[1], command[2])
    elif command[0] == 'end':
        print(list_given)
        break

