odd = False
length = int(input())
i = 0

while odd == False and i <= length: 
    nb = int(input())
    if nb % 2 != 0: 
        print(f'{nb} is odd!')
        odd = True
        break 
    i += 1
    if i == length:
        print('All numbers are even.')
        break
