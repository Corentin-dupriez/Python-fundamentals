actions = input().split('|')
energy = 100
coins = 100
actions_and_values = list()
all_done = True

for action in actions:
    action_and_value = action.split('-')
    actions_and_values.append(action_and_value)

for action_and_value in actions_and_values:
    if action_and_value[0] == 'rest':
        if energy + int(action_and_value[1]) <= 100:
            energy += int(action_and_value[1])
            energy_gained = int(action_and_value[1])
        else:
            energy_gained = 100 - energy
            energy = 100
        print(f'You gained {energy_gained} energy.')
        print(f'Current energy: {energy}.')
    elif action_and_value[0] == 'order':
        if energy - 30 >= 0:
            coins += int(action_and_value[1])
            energy -= 30
            print(f'You earned {action_and_value[1]} coins.')
        else:
            energy += 50
            print('You had to rest!')
    else:
        if coins - int(action_and_value[1]) >= 0:
            print(f'You bought {action_and_value[0]}.')
            coins -= int(action_and_value[1])
        else:
            print(f'Closed! Cannot afford {action_and_value[0]}.')
            all_done = False
            break

if all_done:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
