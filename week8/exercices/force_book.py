def add_user_to_side(force_side: str, user_name: str):
    existing_users = []
    for i in force_users.values():
        for j in i:
            existing_users.append(j)
    if user_name not in existing_users:
        if force_side not in force_users.keys():
            force_users[force_side] = [user_name]
        else:
            force_users[force_side].append(user_name)


def switch_user(force_side: str, user_name: str):
    for sides, users in force_users.items():
        for user in users:
            if user_name == user:
                force_users[sides].pop(force_users[sides].index(user_name))
    add_user_to_side(force_side, user_name)
    print(f'{user_name} joins the {force_side} side!')


def print_force_users(users: dict):
    for sides, users in users.items():
        if users:
            print(f'Side: {sides}, Members: {len(users)}')
            for user in users:
                print(f'! {user}')


force_users = {}

while True:
    command = input()
    if command == 'Lumpawaroo':
        break

    if '|' in command:
        side, user = command.split(' | ')
        add_user_to_side(side, user)
    elif '->' in command:
        user, side = command.split(' -> ')
        switch_user(side, user)

print_force_users(force_users)
