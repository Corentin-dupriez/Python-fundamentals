def swap_elements(index1, index2, data_array):
    data_array[index1], data_array[index2] = data_array[index2], data_array[index1]
    return data_array


def multiply_elements(index1, index2, data_array):
    data_array[index1] = data_array[index1] * data_array[index2]
    return data_array


def decrease_elements(data_array):
    for element in range(len(data_array)):
        data_array[element] -= 1
    return data_array


array = list(map(int, input().split()))
command = input().split()

while command[0] != 'end':
    if command[0] == 'swap':
        array = swap_elements(int(command[1]), int(command[2]), array)
    elif command[0] == 'multiply':
        array = multiply_elements(int(command[1]), int(command[2]), array)
    elif command[0] == 'decrease':
        array = decrease_elements(array)
    command = input().split()

print(', '.join(list(map(str, array))))
