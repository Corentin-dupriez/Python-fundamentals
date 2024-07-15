string_with_explosion = input()

force = 0

for char in range(len(string_with_explosion)):
    if not string_with_explosion[char].isdigit() and string_with_explosion[char-1] != '>':
        if force >= 1 and string_with_explosion[char] != '>':
            force -= 1
        else:
            character = string_with_explosion[char]
            print(string_with_explosion[char], end='')
    else:
        force += int(string_with_explosion[char])
        force -= 1
