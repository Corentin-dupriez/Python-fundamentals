import string


def calculate_first_number(number_to_calc, letter_for_operation):
    if letter_for_operation.isupper():
        result = number_to_calc / int(string.ascii_uppercase.index(letter_for_operation) + 1)
    elif letter_for_operation.islower():
        result = number_to_calc * int(string.ascii_lowercase.index(letter_for_operation) + 1)
    return result


def calculate_last_letter(letter_for_operation, current_calc):
    if letter_for_operation.isupper():
        current_calc -= int(string.ascii_uppercase.index(letter_for_operation) + 1)
    else:
        current_calc += int(string.ascii_lowercase.index(letter_for_operation) + 1)
    return current_calc


def total_calc(first_letter_calc, last_letter_calc, number_calc):
    total = calculate_first_number(int(number_calc), first_letter_calc)
    total = (calculate_last_letter(last_letter_calc, total))
    return total


fun_strings = input().split()
total = 0
for fun_string in fun_strings:
    fun_string.strip()
    first_letter = fun_string[0]
    number = fun_string[1:-1]
    last_letter = fun_string[-1]
    calculation = total_calc(first_letter, last_letter, number)
    total += calculation

print(f'{total:.2f}')
