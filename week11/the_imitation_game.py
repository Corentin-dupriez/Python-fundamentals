def split_string(index_to_split: int, message: str) -> str:
    """Splits a string at a certain index and moves the first substring at the end."""
    new_string = message[index_to_split:] + message[:index_to_split]
    return new_string


def insert_value(index_to_insert: int, value_to_insert: str, message: str) -> str:
    """Inserts a value at a certain index"""
    new_string = message[:index_to_insert] + value_to_insert + message[index_to_insert:]
    return new_string


def change_values(string_to_replace: str, element_to_replace_with: str, message: str) -> str:
    """Replace all instances of an item by another element"""
    while string_to_replace in message:
        index_start = message.index(string_to_replace)
        index_end = index_start + len(string_to_replace)
        message = message[:index_start] + element_to_replace_with + message[index_end:]
    return message


encrypted_message = input()

while True:
    command = input()
    if command == 'Decode':
        break
    split_command = command.split('|')
    if split_command[0] == 'Move':
        index = int(split_command[1])
        encrypted_message = split_string(index, encrypted_message)
    elif split_command[0] == 'Insert':
        index, value = int(split_command[1]), split_command[2]
        encrypted_message = insert_value(index, value, encrypted_message)
    elif split_command[0] == 'ChangeAll':
        substring, replacement = split_command[1], split_command[2]
        encrypted_message = change_values(substring, replacement, encrypted_message)

print(f'The decrypted message is: {encrypted_message}')
