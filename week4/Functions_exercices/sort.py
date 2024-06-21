def sort_num(lst):
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    lst = sorted(lst)
    print(lst)


nums = input().split(' ')
sort_num(nums)
