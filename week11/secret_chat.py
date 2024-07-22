def insert_a_space(command_to_read: str, message: str):
    index_to_insert = int(command_to_read.split(':|:')[1])
    new_message = message[:index_to_insert] + ' ' + message[index_to_insert:]
    print(new_message)
    return new_message


def reverse_string(command_to_read: str, message: str):
    substring = command_to_read.split(':|:')[1]
    if substring in message:
        start_index = message.index(substring)
        end_index = start_index + len(substring)
        message = message[0:start_index] + message[end_index:] + substring[::-1]
        print(message)
    else:
        print('error')
    return message


def change_all(command_to_read: str, message: str):
    command, substring, replacement = command_to_read.split(':|:')
    while substring in message:
        index_start = message.index(substring)
        index_end = index_start + len(substring)
        message = message[:index_start] + replacement + message[index_end:]
    print(message)
    return message


concealed_message = input()

while True:
    command = input()
    if command == 'Reveal':
        break
    if 'InsertSpace' in command:
        concealed_message = insert_a_space(command, concealed_message)
    if 'Reverse' in command:
        concealed_message = reverse_string(command, concealed_message)
    if 'ChangeAll' in command:
        concealed_message = change_all(command, concealed_message)


print(f'You have a new text message: {concealed_message}')
