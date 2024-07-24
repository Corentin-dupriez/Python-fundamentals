import re

pattern = r'@(([a-zA-Z]{3,})@@([a-zA-Z]{3,}))@|#(([a-zA-Z]{3,})##([a-zA-Z]{3,}))#'
text = input()
matches = re.findall(pattern, text)
all_words = [(x[1], x[2]) if x[1] else (x[4], x[5]) for x in matches]
mirror_words = []
for word in all_words:
    if word[0] == word[1][::-1]:
        mirror_words.append(word)
if matches:
    print(f'{len(all_words)} word pairs found!')
else:
    print('No word pairs found!')

if mirror_words:
    print('The mirror words are:')
    for item in range(len(mirror_words)):
        if item < len(mirror_words) - 1:
            print(f'{mirror_words[item][0]} <=> {mirror_words[item][1]}', end=', ')
        else:
            print(f'{mirror_words[item][0]} <=> {mirror_words[item][1]}', end='')
else:
    print('No mirror words!')
