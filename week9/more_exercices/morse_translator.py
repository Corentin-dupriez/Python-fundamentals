def translate_word(morse):
    translated_word = ''
    for letter in morse.split():
        translated_word += translate_letter(letter)
    return translated_word


def translate_letter(morse_letter):
    morse_letters = {'.-': 'A',
                     '-...': 'B',
                     '-.-.': 'C',
                     '-..': 'D',
                     '.': 'E',
                     '..-.': 'F',
                     '--.': 'G',
                     '....': 'H',
                     '..': 'I',
                     '.---': 'J',
                     '-.-': 'K',
                     '.-..': 'L',
                     '--': 'M',
                     '-.': 'N',
                     '---': 'O',
                     '.--.': 'P',
                     '.-.': 'R',
                     '...': 'S',
                     '-': 'T',
                     '..-': 'U',
                     '...-': 'V',
                     '.--': 'W',
                     '-..-': 'X',
                     '-.--': 'Y',
                     '--..': 'Z'}
    return morse_letters[morse_letter]


morse_words = input().split(' | ')
translated_sentence = ''
for morse_word in morse_words:
    word = translate_word(morse_word)
    translated_sentence += word
    translated_sentence += ' '

print(translated_sentence)
