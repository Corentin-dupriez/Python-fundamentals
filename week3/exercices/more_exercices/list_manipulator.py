def exchange(index):
    if 0 <= index < len(list_given):
        first_part = list_given[index + 1:]
        second_part = list_given[:index + 1]
        return first_part + second_part
    print('Invalid index')
    return list_given


def construct_odd_list():
    list_numbers = [i for i in list_given if i % 2 != 0]
    return list_numbers


def construct_even_list():
    list_numbers = [i for i in list_given if i % 2 == 0]
    return list_numbers


def get_number(min_or_max, list_to_use):
    if min_or_max == 'min':
        number = min(list_to_use)
    else:
        number = max(list_to_use)
    return number


def get_index_of_number(number_to_search):
    for i, j in enumerate(list_given):
        if j == number_to_search:
            max_index = i
    return max_index


def max_nb(odd_or_even):
    number_to_return = None
    if odd_or_even == 'odd':
        list_odds = construct_odd_list()
        if list_odds:
            number_to_return = get_number('max', list_odds)
    else:
        list_evens = construct_even_list()
        if list_evens:
            number_to_return = get_number('max', list_evens)
    if number_to_return:
        return get_index_of_number(number_to_return)
    return 'No matches'


def min_nb(odd_or_even):
    number_to_return = None
    if odd_or_even == 'odd':
        list_odds = construct_odd_list()
        if list_odds:
            number_to_return = get_number('min', list_odds)
    else:
        list_evens = construct_even_list()
        if list_evens:
            number_to_return = get_number('min', list_evens)
    if number_to_return:
        return get_index_of_number(number_to_return)
    return 'No matches'


def first_nb(count_nb, odd_or_even):
    list_numbers = []
    if 0 < int(count_nb) <= len(list_given):
        if odd_or_even == 'odd':
            list_numbers = construct_odd_list()
            return list_numbers[:int(count_nb)]
        else:
            list_numbers = construct_even_list()
            return list_numbers[:int(count_nb)]
        return list_numbers
    return 'Invalid count'


def last_nb(count_nb, odd_or_even):
    list_numbers = []
    if 0 < int(count_nb) <= len(list_given):
        if odd_or_even == 'odd':
            list_numbers = construct_odd_list()
            return list_numbers[-int(count_nb):]
        else:
            list_numbers = construct_even_list()
            return list_numbers[-int(count_nb):]
        return list_numbers
    return 'Invalid count'


list_given = list(map(int, input().split()))

command = input().split()

while command[0] != 'end':
    if command[0] == 'exchange':
        list_given = exchange(int(command[1]))
    elif command[0] == 'max':
        print(max_nb(command[1]))
    elif command[0] == 'min':
        print(min_nb(command[1]))
    elif command[0] == 'first':
        print(first_nb(command[1], command[2]))
    elif command[0] == 'last':
        print(last_nb(command[1], command[2]))
    command = input().split()

print(list_given)
