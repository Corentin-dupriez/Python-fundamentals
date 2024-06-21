first_line = input().split(' ')
second_line = input().split(' ')
third_line = input().split(' ')

if first_line.count('1') == 3 or second_line.count('1') == 3 or third_line.count('1') == 3:
    print('First player won')
elif first_line.count('1') and second_line.count('1') and third_line.count('1') and first_line.index('1') == second_line.index('1') == third_line.index('1'):
    print('First player won')
elif first_line.count('1') and second_line.count('1') and third_line.count('1') and first_line.index('1') == second_line.index('1')-1 == third_line.index('1')-2:
    print('First player won')
elif first_line.count('1') and second_line.count('1') and third_line.count('1') and first_line.index('1') == second_line.index('1') + 1 == third_line.index('1') + 2:
    print('First player won')
elif first_line.count('2') == 3 or second_line.count('2') == 3 or third_line.count('2') == 3:
    print('Second player won')
elif first_line.count('2') and second_line.count('2') and third_line.count('2') and first_line.index('2') == second_line.index('2') == third_line.index('2'):
    print('Second player won')
elif first_line.count('2') and second_line.count('2') and third_line.count('2') and first_line.index('2') == second_line.index('2') - 1 == third_line.index('2') - 2:
    print('Second player won')
elif first_line.count('2') and second_line.count('2') and third_line.count('2') and first_line.index('2') == second_line.index('2') + 1 == third_line.index('2') + 2:
    print('Second player won')
else:
    print('Draw!')
