targets = list(map(int, input().split()))
command = input().split()

while command[0] != 'End':
    if command[0] == 'Shoot':
        if 0 <= int(command[1]) < len(targets):
            targets[int(command[1])] -= int(command[2])
            if targets[int(command[1])] <= 0:
                targets.pop(int(command[1]))
    elif command[0] == 'Strike':
        if 0 <= int(command[1]) < len(targets) and (0 <= int(command[1]) - int(command[2])) and len(targets) >= int(command[1]) + int(command[2]):
            for i in range(int(command[1]) + int(command[2]), int(command[1]) - int(command[2]) - 1, -1):
                targets.pop(i)
        else:
            print('Strike missed!')
    elif command[0] == 'Add':
        if 0 <= int(command[1]) < len(targets):
            targets.insert(int(command[1]), int(command[2]))
        else:
            print('Invalid placement!')
    command = input().split()

targets = list(map(str, targets))
print('|'.join(targets))
