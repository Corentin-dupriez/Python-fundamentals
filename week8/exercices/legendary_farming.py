def check_achieved(artifacts: dict):
    for item, quantity in artifacts.items():
        if quantity >= 250 and item in ('shards', 'fragments', 'motes'):
            return item


def discover_artifact(material: str, all_mat: dict):
    if material == 'shards':
        print('Shadowmourne obtained!')
    elif material == 'fragments':
        print('Valanyr obtained!')
    else:
        print('Dragonwrath obtained!')
    all_mat[material] -= 250
    for item, quantity in all_mat.items():
        print(f'{item}: {quantity}')


all_materials = {'shards': 0, 'fragments': 0, 'motes': 0}

while not check_achieved(all_materials):
    list_materials = input().split()

    for i in range(0, len(list_materials), 2):
        if list_materials[i+1].lower() in all_materials.keys():
            all_materials[list_materials[i+1].lower()] += int(list_materials[i])
            if all_materials[list_materials[i+1].lower()] >= 250:
                break
        else:
            all_materials[list_materials[i + 1].lower()] = int(list_materials[i])
            if all_materials[list_materials[i+1].lower()] >= 250:
                break


discover_artifact(check_achieved(all_materials), all_materials)
