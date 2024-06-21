def find_perfect_number(num):
    divisors = list()
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    if sum(divisors) == num:
        print('We have a perfect number!')
    else:
        print('It\'s not so perfect.')


number = int(input())
find_perfect_number(number)
