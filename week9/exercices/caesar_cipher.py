string_to_encrypt = input()
encrypted = ''

for char in string_to_encrypt:
    encrypted += chr(ord(char) + 3)

print(encrypted)
