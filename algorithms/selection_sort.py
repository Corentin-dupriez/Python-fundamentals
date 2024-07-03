array = [2, 23, 10, 1]
sorted_array = []

for i in range(len(array)):
    min_element = None
    for j in range(len(array)):
        if not min_element:
            min_element = array[j]
        elif array[j] < min_element:
            min_element = array[j]
    array.pop(array.index(min_element))
    sorted_array.append(min_element)

print(sorted_array)
