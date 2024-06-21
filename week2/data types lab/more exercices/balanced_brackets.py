lines = int(input())
nb_brackets = 0
balanced = True
previous_bracket = None

for line in range(lines):
    char = str(input())
    if char in ('(', ')'):
        bracket = char
        if (not previous_bracket and bracket == ')') or bracket == previous_bracket:
            balanced = False
        previous_bracket = bracket

if balanced:
    print('BALANCED')
else:
    print('UNBALANCED')
