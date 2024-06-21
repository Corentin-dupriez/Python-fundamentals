def ascii_in_range():
    ascii_list = list()
    low_range = ord(input())
    high_range = ord(input())
    for i in range(low_range +1, high_range):
        ascii_list.append(chr(i))
    print(' '.join(ascii_list))


ascii_in_range()
