numbers = map(int, input().split(' '))

even_numbers = list(filter(lambda n: n % 2 == 0, numbers))

print(even_numbers)
