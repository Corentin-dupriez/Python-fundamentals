def is_palindrome(num):
    if num == num[::-1]:
        print('True')
    else:
        print('False')


list_integers = input().split(', ')
for integer in list_integers:
    is_palindrome(integer)
