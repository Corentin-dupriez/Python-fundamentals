current_year = int(input()) + 1
happy_year = False

while not happy_year:
    unique_digit = True
    year = list(str(current_year))
    for digit in year:
        if year.count(digit) > 1:
            unique_digit = False
    if not unique_digit:
        current_year += 1
    elif unique_digit:
        happy_year = True
        break

if happy_year:
    print(current_year)

