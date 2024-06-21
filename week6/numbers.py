nums = list(map(int, input().split()))

average = sum(nums) / len(nums)

bigger_nums = [x for x in nums if x > average]

bigger_nums = sorted(bigger_nums, reverse=True)

if bigger_nums:
    for num in bigger_nums[:5]:
        print(num, end=' ')
else:
    print('No')
