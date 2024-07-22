import re


def count_key(message_to_analyze: str):
    key = 0
    for character in message_to_analyze:
        if character.lower() in ['a', 's', 't', 'r']:
            key += 1
    return key


def decode_message(message_to_decode: str):
    pattern = r'@([A-Z]{1}[a-z]+)\w?:(\d+)!([AD])!->(\d+)'
    matches = re.search(pattern, message_to_decode)
    if matches:
        planet, population, attack, soldiers = matches.groups()
        attack_planet(planet, attack)


def attack_planet(planet: str, type_attack: str):
    if type_attack == 'A':
        attacked_planets.append(planet)
    elif type_attack == 'D':
        destroyed_planets.append(planet)


def translate_message(message_to_translate: str, key: int):
    translated_message = ''
    for char in message_to_translate:
        translated_message += chr(ord(char)-key)
    return translated_message


def print_planets(list_planet: list, type_attack: str):
    if type_attack == 'attacked':
        print(f'Attacked planets:', end=' ')
    else:
        print(f'Destroyed planets:', end=' ')
    print(len(list_planet))
    for planet in list_planet:
        print(f'-> {planet}')


attacked_planets = []
destroyed_planets = []

messages = int(input())
for _ in range(messages):
    message = input()
    translation_key = count_key(message)
    translated = translate_message(message, translation_key)
    decode_message(translated)

print_planets(sorted(attacked_planets), 'attacked')
print_planets(sorted(destroyed_planets), 'destroyed')
