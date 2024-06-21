def calculate_factorial(number):
    for current_num in range(1, number):
        number *= current_num
    return number


def factorial_division(num1, num2):
    fact_1 = calculate_factorial(num1)
    fact_2 = calculate_factorial(num2)
    division_result = fact_1 / fact_2
    return f'{division_result:.2f}'


nb1 = int(input())
nb2 = int(input())


print(factorial_division(nb1, nb2))
