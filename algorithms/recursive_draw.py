def draw(n):
    if n == 0:
        return
    # Pre-action: print n asterisks
    print('*' * n)
    draw(n - 1)
    # Post-action: print n hashtags
    print('#' * n)


draw(5)
