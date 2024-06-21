def tribonacci(length):
    sequence = [1]
    for i in range(1, length):
        if len(sequence) < 3:
            number = sum(sequence)
            sequence.append(number)
        else:
            number = sum(sequence[i-3:i + 1])
            sequence.append(number)
    for num in sequence:
        print(num, end=' ')


length_sequence = int(input())
tribonacci(length_sequence)
