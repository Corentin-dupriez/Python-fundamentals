word = str(input().upper())
words_to_find = ['SAND', 'WATER', 'FISH', 'SUN']
total_found = 0

for i in words_to_find:
    if i in word:
        total_found += word.count(i)

print(total_found)


