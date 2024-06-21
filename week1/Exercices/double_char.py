word = input()
word_double = []

while word != 'End':
    if word != 'SoftUni':
        for i in word:
            word_double.append(i * 2)
        print(''.join(word_double))
    word_double = []
    word = input()
