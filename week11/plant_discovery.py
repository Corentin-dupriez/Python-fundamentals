def add_plant(plant_name, rarity):
    if is_plant_in_list(plant_name):
        for element in all_plants:
            if element['name'] == plant_name:
                element['rarity'] = rarity
    else:
        all_plants.append({'name': plant_name, 'rarity': rarity})


def is_plant_in_list(plant_name):
    for element in all_plants:
        if element['name'] == plant_name:
            return True
    return False


def rate_plant(plant_name, plant_rating):
    found = False
    for element in all_plants:
        if element['name'] == plant_name:
            found = True
            if not element.get('rating'):
                element['rating'] = [plant_rating]
            else:
                element['rating'].append(plant_rating)
    if not found:
        print('error')


def update_plant(plant_name, new_plant_rarity):
    found = False
    for element in all_plants:
        if element['name'] == plant_name:
            found = True
            element['rarity'] = new_plant_rarity
    if not found:
        print('error')


def reset_plant(plant_name):
    found = False
    for element in all_plants:
        if element['name'] == plant_name:
            found = True
            if element['rating']:
                element['rating'] = []
    if not found:
        print('error')


nb_plants = int(input())
all_plants = []

for _ in range(nb_plants):
    name, plant_rarity = input().split('<->')
    add_plant(name, int(plant_rarity))


while True:
    command = input()
    if command == 'Exhibition':
        break
    action, arguments = command.split(': ')
    if action == 'Rate':
        name, rating = arguments.split(' - ')
        rate_plant(name, int(rating))
    elif action == 'Update':
        name, new_rarity = arguments.split(' - ')
        update_plant(name, int(new_rarity))
    elif action == 'Reset':
        name = arguments
        reset_plant(name)

print('Plants for the exhibition:')
for plant in all_plants:
    if plant.get('rating'):
        print(f'- {plant["name"]}; Rarity: {plant["rarity"]}; Rating: {sum(plant["rating"])/len(plant["rating"]):.2f}')
    else:
        print(f'- {plant["name"]}; Rarity: {plant["rarity"]}; Rating: 0.00')
