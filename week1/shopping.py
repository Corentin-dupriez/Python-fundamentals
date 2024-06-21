budget = int(input())
amount = 0 

while amount <= budget: 
    command = input()
    if command == 'End': 
        print('You bought everything needed.')
        break
    elif command.isnumeric(): 
        amount += int(command)
    if amount > budget:
        print('You went in overdraft!')