import string

sentence = input()
alphabetical_chars = string.ascii_letters
symbols = string.punctuation

for char in range(len(sentence)):
    if sentence[char] == ':' and (sentence[char+1] in alphabetical_chars or sentence[char+1] in symbols):
        print(sentence[char:char+2])
        