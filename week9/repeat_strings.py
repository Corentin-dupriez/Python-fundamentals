strings_to_repeat = input().split()

for string_to_repeat in strings_to_repeat:
    print(string_to_repeat*len(string_to_repeat), end='')
