def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle_index = (left + right) // 2
        middle_element = nums[middle_index]

        if middle_element == target:
            return middle_index

        if target > middle_element:
            left = middle_index + 1
        else:
            right = middle_index - 1


x = 999999
list_search = [x for x in range(1, 1000000)]

print(binary_search(list_search, x))

