word1, word2 = input().split()
max_length = max([len(word1), len(word2)])
min_length = min([len(word1), len(word2)])
total = 0

for i in range(min_length):
    total += ord(word1[i]) * ord(word2[i])

for j in range(min_length, max_length):
    if max_length > len(word1):
        total += ord(word2[j])
    elif max_length > len(word2):
        total += ord(word1[j])

print(total)
