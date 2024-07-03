array = [2, 23, 10, 1]

for i in range(len(array)):
    for j in range(len(array)):
        if 0 < j+1 < len(array):
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]

print(array)
