def print_resources(res: dict):
    for i, j in res.items():
        print(f'{i} -> {j}')


line_nb = 1
resources = {}
last_resource = None

while True:
    command = input()
    if command == 'stop':
        break
    elif line_nb % 2 != 0:
        if command not in resources.keys():
            resources[command] = 0
        last_resource = command
    else:
        resources[last_resource] += int(command)
    line_nb += 1

print_resources(resources)
