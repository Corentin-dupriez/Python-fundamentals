key = int(input())
lines = int(input())
word = []

for line in range(lines):
    character = input()
    char_ascii = ord(character)
    character = chr(char_ascii + key)
    word.append(character)

print(''.join(word))
