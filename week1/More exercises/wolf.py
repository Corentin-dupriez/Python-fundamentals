animals = str(input())

animals_list = animals.split(', ')

if animals_list[-1] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    for i in range(len(animals_list)-1, -1, -1):
        if animals_list[i] == 'sheep' and animals_list[i-1] == 'wolf':
            print(f'Oi! Sheep number {len(animals_list) - i}! You are about to be eaten by a wolf!')
