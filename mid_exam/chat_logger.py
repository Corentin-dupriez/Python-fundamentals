def chat(message):
    """Adds a message to the chat"""
    all_messages.append(message)


def delete_message(message):
    """Deletes a message from the chat if it exists"""
    if message in all_messages:
        all_messages.pop(all_messages.index(message))


def edit_message(original, edited):
    """Edits an existing message if it is found in the chat"""
    if original in all_messages:
        all_messages[all_messages.index(original)] = edited


def pin_message(message):
    """Pops a message and adds it to the end of the chat"""
    if message in all_messages:
        all_messages.append(all_messages.pop(all_messages.index(message)))


def spam_chat(messages):
    for message in messages:
        all_messages.append(message)


command = input().split()
all_messages = []

while command[0] != 'end':
    if command[0] == 'Chat':
        chat(command[1])
    elif command[0] == 'Delete':
        delete_message(command[1])
    elif command[0] == 'Edit':
        edit_message(command[1], command[2])
    elif command[0] == 'Pin':
        pin_message(command[1])
    elif command[0] == 'Spam':
        spam_chat(command[1:])
    command = input().split()

for msg in all_messages:
    print(msg)
