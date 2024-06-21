def odd_even_sum():
    evens = list()
    odds = list()
    numbers = input()
    for number in numbers:
        if int(number) % 2 == 0:
            evens.append(int(number))
        else:
            odds.append(int(number))
    print(f'Odd sum = {sum(odds)}, Even sum = {sum(evens)}')


odd_even_sum()
