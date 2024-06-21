divisor = int(input())
bound = int(input())
divisible = []

for i in range(1, bound+1): 
    if i % divisor == 0: 
        divisible.append(i)

greater_divisible = divisible[-1]
print(greater_divisible)