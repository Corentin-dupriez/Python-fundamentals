treasure_chest = input().split('|')
command = input().split()

while command[0] != 'Yohoho!':
    if 'Loot' in command:
        for item in range(1, len(command)):
            if command[item] not in treasure_chest:
                treasure_chest.insert(0, command[item])
    elif 'Drop' in command:
        if int(command[1]) >= len(treasure_chest):
            pass
        else:
            removed_item = treasure_chest.pop(int(command[1]))
            treasure_chest.append(removed_item)
    elif 'Steal' in command:
        print(', '.join(treasure_chest[-int(command[1])::]))
        treasure_chest = treasure_chest[:-int(command[1])]
    command = input().split()

if not treasure_chest:
    print('Failed treasure hunt.')
else:
    length_chest = 0
    for item in treasure_chest:
        length_chest += len(item)
    gain = length_chest / len(treasure_chest)
    print(f'Average treasure gain: {gain:.2f} pirate credits.')
