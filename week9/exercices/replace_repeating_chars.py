string_to_replace = input()
new_string = ''

for char in range(len(string_to_replace)):
    if char != 0 and string_to_replace[char] == string_to_replace[char-1]:
        pass
    else:
        new_string += string_to_replace[char]

print(new_string)
