chars = int(input())
total_ascii_chars = 0

for char in range(chars):
    char = input()
    ascii_char = ord(char)
    total_ascii_chars += ascii_char

print(f'The sum equals: {total_ascii_chars}')
