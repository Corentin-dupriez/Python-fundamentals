def blacklist_friend(name):
    """Blacklists a friend if the index is found"""
    if name in friends:
        friends[friends.index(name)] = 'Blacklisted'
        print(f'{name} was blacklisted.')
        return 1
    else:
        print(f'{name} was not found.')
        return 0


def error_friend(index):
    """Changes a friend to Lost if the index is found and not blacklisted or lost"""
    if 0 <= index < len(friends) and friends[index] != 'Blacklisted' and friends[index] != 'Lost':
        lost_friend = friends[index]
        friends[index] = 'Lost'
        print(f'{lost_friend} was lost due to an error.')
        return 1
    return 0


def change_friend(index, name):
    """Changes the username of a friend if the index is in the array"""
    if 0 <= index < len(friends):
        current_name = friends[index]
        friends[index] = name
        print(f'{current_name} changed his username to {name}.')


friends = input().split(', ')

command = input().split()
blacklisted = 0
lost = 0

while command[0] != 'Report':
    if command[0] == 'Blacklist':
        blacklisted_friend = blacklist_friend(command[1])
        blacklisted += blacklisted_friend
    elif command[0] == 'Error':
        error_friend_return = error_friend(int(command[1]))
        lost += error_friend_return
    elif command[0] == 'Change':
        change_friend(int(command[1]), command[2])
    command = input().split()

print(f'Blacklisted names: {blacklisted}')
print(f'Lost names: {lost}')
print(' '.join(friends))
