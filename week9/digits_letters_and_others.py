string_to_filter = input()
letters = ''
digits = ''
specials = ''

for character in string_to_filter:
    if character.isdigit():
        digits += character
    elif character.isalpha():
        letters += character
    else:
        specials += character

print(digits)
print(letters)
print(specials)
