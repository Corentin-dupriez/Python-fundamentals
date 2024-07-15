banned_words = input().split(', ')
text_to_filter = input()

for banned_word in banned_words:
    while banned_word in text_to_filter:
        text_to_filter = text_to_filter.replace(banned_word, '*' * len(banned_word))

print(text_to_filter)
