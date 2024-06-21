n = int(input())
i = 0

while i < n: 
    message = int(input())
    if message == 88: 
        print('Hello')
    elif message == 86: 
        print('How are you?')
    elif message < 88: 
        print('GREAT!')
    elif message > 88: 
        print('Bye.')
    i += 1