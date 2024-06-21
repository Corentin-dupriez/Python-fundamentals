gifts = input().split(' ')
command = input()
new_gifts = []

while command != 'No money':
    command_type = command.split(' ')
    if command_type[0] == 'OutOfStock':
        while command_type[1] in gifts:
            gifts[gifts.index(command_type[1])] = 'None'
    elif command_type[0] == 'Required' and 0 <= int(command_type[2]) <= len(gifts) - 1:
        gifts[int(command_type[2])] = command_type[1]
    elif command_type[0] == 'JustInCase':
        gifts[-1] = command_type[1]
    elif command == 'No Money':
        break
    command = input()

for gift in gifts:
    if gift != 'None':
        new_gifts.append(gift)

print(' '.join(new_gifts))
