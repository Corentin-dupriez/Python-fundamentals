number = int(input())
prime = True

for i in range(1, number):
    for j in range(1, number):
        if i * j == number:
            prime = False

if prime:
    print('True')
else:
    print('False')
