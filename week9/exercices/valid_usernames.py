def is_good_length(name):
    if 3 <= len(name) <= 16:
        return name


def correct_characters(name):
    for char in name:
        if not char.isdigit() and not char.isalpha() and char not in ('-', '_'):
            return False
    return True


def redundant_symbol(name):
    if ' ' in name:
        return False
    return True


def is_username_valid(name):
    if is_good_length(name):
        if correct_characters(name):
            if redundant_symbol(name):
                return True
    return False


usernames = input().split(', ')

for username in usernames:
    if is_username_valid(username):
        print(username)
