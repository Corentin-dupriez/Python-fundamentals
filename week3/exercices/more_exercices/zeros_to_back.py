numbers = input().split(', ')

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

for number in numbers:
    if number == 0:
        numbers.append(numbers.pop(numbers.index(number)))


print(numbers)
