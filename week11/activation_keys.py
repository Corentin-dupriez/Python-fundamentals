def key_contains(sub_string, key):
    if sub_string in key:
        print(f'{key} contains {sub_string}')
    else:
        print('Substring not found!')


def slice_key(start_index, end_index, key):
    new_key = key[:start_index] + key[end_index:]
    print(new_key)
    return new_key


def flip_key(up_low, start_index, end_index, key):
    if up_low == 'Upper':
        extracted = key[start_index:end_index].upper()
    elif up_low == 'Lower':
        extracted = key[start_index:end_index].lower()
    new_key = key[:start_index] + extracted + key[end_index:]
    print(new_key)
    return new_key


raw_key = input()
activation_key = raw_key

while True:
    command = input()
    if command == 'Generate':
        break
    if command.split('>>>')[0] == 'Contains':
        action, substring = command.split('>>>')
        key_contains(substring, activation_key)
    elif command.split('>>>')[0] == 'Flip':
        action, up_or_low, start, end = command.split('>>>')
        activation_key = flip_key(up_or_low, int(start), int(end), activation_key)
    elif command.split('>>>')[0] == 'Slice':
        action, start, end = command.split('>>>')
        activation_key = slice_key(int(start), int(end), activation_key)

print(f'Your activation key is: {activation_key}')
