digits = input().split(' ')
index = 0

characters = input()
char_list = list()

message = list()

for digit in digits:
    calc_nb = 0
    for number in digit:
        calc_nb += int(number)
    digits[index] = calc_nb
    index += 1

for character in characters:
    char_list.append(character)

for char_to_find in digits:
    char_searched = 0
    index_in_list = 0
    while char_searched < char_to_find:
        if index_in_list == len(char_list):
            index_in_list = 0
        char_searched += 1
        index_in_list += 1
    message.append(char_list.pop(index_in_list))

print(''.join(message))
