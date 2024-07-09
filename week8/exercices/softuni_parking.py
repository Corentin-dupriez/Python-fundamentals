def register_user(user: str, license_nb: str) -> str:
    if parking.get(user):
        return f'ERROR: already registered with plate number {license_nb}'
    parking[user] = license_nb
    return f'{user} registered {license_nb} successfully'


def unregister_user(user: str):
    if not parking.get(user):
        return f'ERROR: user {user} not found'
    parking.pop(user)
    return f'{user} unregistered successfully'


def print_registered(parking_list: dict):
    for person, number in parking_list.items():
        print(f'{person} => {number}')


parking = dict()

nb_commands = int(input())

for _ in range(nb_commands):
    command = input().split()
    if command[0] == 'register':
        username = command[1]
        license_plate = command[2]
        print(register_user(username, license_plate))
    elif command[0] == 'unregister':
        username = command[1]
        print(unregister_user(username))

print_registered(parking)
