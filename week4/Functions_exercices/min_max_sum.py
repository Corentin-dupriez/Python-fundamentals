def min_max_sum(lst):
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    min_nm = min(lst)
    max_nm = max(lst)
    print(f'The minimum number is {min_nm} \nThe maximum number is {max_nm}\nThe sum number is: {sum(lst)}')


list_of_nums = input().split(' ')
min_max_sum(list_of_nums)
