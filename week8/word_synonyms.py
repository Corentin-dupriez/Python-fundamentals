count_words = int(input())
word_list = {}

for i in range(count_words):
    word = input()
    synonym = input()
    if word in word_list:
        word_list[word].append(synonym)
    else:
        word_list[word] = [synonym]

for word in word_list:
    print(f'{word} - {", ".join(word_list[word])}')
