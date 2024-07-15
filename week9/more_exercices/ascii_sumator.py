def is_char_between_chars(char_to_find, upper_boundary, lower_boundary):
    char_in_ascii = ord(char_to_find)
    upper_boundary_in_ascii = ord(upper_boundary)
    lower_boundary_in_ascii = ord(lower_boundary)
    if lower_boundary_in_ascii < char_in_ascii < upper_boundary_in_ascii:
        return char_in_ascii


first_char = input()
second_char = input()
characters_to_find = input()
ascii_sum = 0

for char in characters_to_find:
    number_to_add = is_char_between_chars(char, second_char, first_char)
    if number_to_add:
        ascii_sum += number_to_add

print(ascii_sum)
