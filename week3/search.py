sentences = int(input())
word_searched = input()

all_sentences = [input() for i in range(sentences)]
filtered_sentences = []

for i in all_sentences:
    if word_searched in i:
        filtered_sentences.append(i)

print(all_sentences)
print(filtered_sentences)
