import string


def check_pwd(pwd):
    valid_pwd = True
    total_digits = 0
    non_digit_letters_chars = 0
    digits = string.digits
    digits_and_letters = string.ascii_letters + string.digits
    for char in pwd:
        if char in digits:
            total_digits += 1
        elif char not in digits_and_letters:
            non_digit_letters_chars += 1
    if len(pwd) < 6 or len(pwd) > 10:
        print('Password must be between 6 and 10 characters')
        valid_pwd = False
    if non_digit_letters_chars > 0:
        print('Password must consist only of letters and digits')
        valid_pwd = False
    if total_digits < 2:
        print('Password must have at least 2 digits')
        valid_pwd = False
    if valid_pwd:
        print('Password is valid')


password = input()
check_pwd(password)
