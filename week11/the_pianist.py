def add_piece(piece_to_add: str):
    already_present = False
    action, name, composer, key = piece_to_add.split('|')
    for piece_name in pieces.keys():
        if piece_name == name:
            print(f'{piece_name} is already in the collection!')
            already_present = True
            break
    if not already_present:
        pieces[name] = {'composer': composer, 'key': key}
        print(f'{name} by {composer} in {key} added to the collection!')


def remove_piece(piece_to_remove: str):
    to_remove = piece_to_remove.split('|')[1]
    if pieces.get(to_remove):
        pieces.pop(to_remove)
        print(f'Successfully removed {to_remove}!')
    else:
        print(f'Invalid operation! {to_remove} does not exist in the collection.')


def change_key(piece_to_change: str):
    action, piece, new_key = piece_to_change.split('|')
    if pieces.get(piece):
        pieces[piece]['key'] = new_key
        print(f'Changed the key of {piece} to {new_key}!')
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')


nb_pieces = int(input())
pieces = dict()

for _ in range(nb_pieces):
    name, composer, key = input().split('|')
    pieces[name] = {'composer': composer, 'key': key}

while True:
    command = input()
    if command == 'Stop':
        break
    elif 'Add' in command:
        add_piece(command)
    elif 'Remove' in command:
        remove_piece(command)
    elif 'ChangeKey' in command:
        change_key(command)
for piece, piece_info in pieces.items():
    print(f'{piece} -> Composer: {piece_info["composer"]}, Key: {piece_info["key"]}')
