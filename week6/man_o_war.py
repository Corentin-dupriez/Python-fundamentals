def attack_warship(start_index, damage, ship, end_index=None):
    if ship == 'warship':
        if warship[start_index] - damage <= 0:
            return True
        else:
            warship[start_index] -= damage
    elif ship == 'pirate':
        for i in range(start_index, end_index + 1):
            if pirate_ship[i] - damage <= 0:
                return True
            else:
                pirate_ship[i] -= damage


def repair_ship(index, health):
    if pirate_ship[index]+health < 70:
        pirate_ship[index] += health
    else:
        pirate_ship[index] = 70


def get_ship_status():
    sections_to_repair = 0
    for i in range(len(pirate_ship)):
        if pirate_ship[i] < max_health * 0.2:
            sections_to_repair += 1
    return sections_to_repair


pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
max_health = int(input())
warship_won = False
pirate_won = False

command = input().split()

while command[0] != 'Retire' and not warship_won and not pirate_won:
    if command[0] == 'Fire':
        if 0 <= int(command[1]) < len(warship):
            attack = attack_warship(int(command[1]), int(command[2]), 'warship')
            if attack:
                pirate_won = True
                break
    elif command[0] == 'Defend':
        if 0 <= int(command[1]) < len(pirate_ship) and 0 <= int(command[2]) < len(pirate_ship):
            defend = attack_warship(int(command[1]), int(command[3]), 'pirate', int(command[2]))
            if defend:
                warship_won = True
                break
    elif command[0] == 'Repair':
        repair_ship(int(command[1]), int(command[2]))
    elif command[0] == 'Status':
        print(f'{get_ship_status()} sections need repair.')
    command = input().split()

if warship_won:
    print('You lost! The pirate ship has sunken.')
elif pirate_won:
    print('You won! The enemy ship has sunken.')
else:
    print(f'Pirate ship status: {sum(pirate_ship)}\nWarship status: {sum(warship)}')
