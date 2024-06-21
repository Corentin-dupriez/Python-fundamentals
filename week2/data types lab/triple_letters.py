char_nb = int(input())

for i in range(char_nb):
    for j in range(char_nb):
        for k in range(char_nb):
            print(f'{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}')
