def translate_phrase(key: list, phrase_to_translate: str):
    index = 0
    translated_phrase = ''
    for char in phrase_to_translate:
        if index == len(key):
            index = 0
        translated_phrase += chr(ord(char) - int(key[index]))
        index += 1
    return translated_phrase


def decipher_phrase(translated_phrase: str):
    record_treasure = False
    type_treasure = ''
    position_treasure = ''
    record_position = False
    for char in translated_phrase:
        if char == '&' and not record_treasure:
            record_treasure = True
        elif record_treasure and char != '&':
            type_treasure += char
        elif record_treasure and char == '&':
            record_treasure = False
        elif char == '<':
            record_position = True
        elif record_position and char != '>':
            position_treasure += char
        elif char == '>' and record_position:
            record_position = False
    return type_treasure, position_treasure


keys = input().split()

while True:
    phrase = input()
    if phrase == 'find':
        break
    type_of_treasure, position = decipher_phrase(translate_phrase(keys, phrase))
    print(f'Found {type_of_treasure} at {position}')
