command = input()
events = ['coding', 'dog', 'cat', 'movie']
coffee = 0

while command != 'END':
    if command.lower() in events:
        if command.isupper():
            coffee += 2
        else:
            coffee += 1
    command = input()
if coffee <= 5:
    print(coffee)
else:
    print('You need extra sleep')
