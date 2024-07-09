def count_characters(str_to_check: str) -> dict:
    all_chars = {}
    for char in str_to_check:
        if char != ' ':
            if char not in all_chars.keys():
                all_chars[char] = 1
            else:
                all_chars[char] += 1
    return all_chars


def print_chars_and_nb(characters_to_show: dict):
    for i, j in characters_to_show.items():
        print(f'{i} -> {j}')


str_to_read = input()
characters = count_characters(str_to_read)
print_chars_and_nb(characters)
