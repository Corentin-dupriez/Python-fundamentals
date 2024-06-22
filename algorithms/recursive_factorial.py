def calculate_fact(n):
    if n == 0:
        return 1
    return n * calculate_fact(n - 1)


print(calculate_fact(5))
