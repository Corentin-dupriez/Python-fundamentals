a = int(input())
b = int(input())

print(f"""
Before:
a = {a}
b = {b}
""", end='')

c = b
b = a
a = c


print(f"""After:
a = {a}
b = {b}
""")
