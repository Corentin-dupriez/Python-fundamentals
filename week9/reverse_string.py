while True:
    word_to_reverse = input()
    if word_to_reverse == 'end':
        break
    print(f'{word_to_reverse} = {word_to_reverse[::-1]}')