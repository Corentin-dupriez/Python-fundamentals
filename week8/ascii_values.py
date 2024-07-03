characters = input().split(', ')
character_and_ascii = {}

for character in characters:
    character_and_ascii[character] = ord(character)

print(character_and_ascii)