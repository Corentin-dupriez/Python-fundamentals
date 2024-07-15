message = input()

message_to_return = ''
repetitions = ''
all_chars = set()
final_message = ''

for char in range(len(message)):
    if not message[char].isdigit():
        message_to_return += message[char].upper()
        all_chars.add(message[char].upper())
    else:
        for i in range(char, len(message)):
            if message[i].isdigit():
                repetitions += message[i]
            else:
                break
        final_message += message_to_return * int(repetitions)
        message_to_return = ''
        repetitions = ''

print(f'Unique symbols used: {len(all_chars)}')
print(final_message)
