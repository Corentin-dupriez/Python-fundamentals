def calculate():
    operator = input()
    int_one = int(input())
    int_two = int(input())
    if operator == 'multiply':
        calculation = int_one * int_two
    elif operator == 'divide':
        calculation = int(int_one / int_two)
    elif operator == 'add':
        calculation = int_one + int_two
    elif operator == 'subtract':
        calculation = int_one - int_two
    print(calculation)


calculate()
