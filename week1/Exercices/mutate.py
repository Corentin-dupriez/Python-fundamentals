word_one = input()
word_two = input()

for letter in range(len(word_one)):
    if word_one[letter] != word_two[letter]:
        word_three = word_two[:letter + 1] + word_one[letter + 1:]
        print(word_three)

