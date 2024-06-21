numbers = input().split(' ')
to_remove = int(input())
smaller_number = 0

for number in range(len(numbers)):
    numbers[number] = int(numbers[number])

for _ in range(to_remove):
    numbers.pop(numbers.index(min(numbers)))

for number in range(len(numbers)):
    numbers[number] = str(numbers[number])

print(', '.join(numbers))