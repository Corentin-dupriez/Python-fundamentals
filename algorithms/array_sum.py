def sum_array(array, index):
    if index == len(array) - 1:
        return array[index]
    return array[index] + sum_array(array, index+1)


numbers = list(map(int, input().split()))
print(sum_array(numbers, 0))
