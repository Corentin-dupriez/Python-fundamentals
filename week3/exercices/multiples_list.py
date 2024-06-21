factor = int(input())
length = int(input())

factor_list = [x * factor for x in range(1, length + 1)]
print(factor_list)
