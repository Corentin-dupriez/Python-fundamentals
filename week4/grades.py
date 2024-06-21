def rate(note):
    if 2 <= note <= 2.99:
        print('Fail')
    elif note < 3.50:
        print('Poor')
    elif note < 4.5:
        print('Good')
    elif note < 5.5:
        print('Very Good')
    else:
        print('Excellent')


grade = float(input())
rate(grade)
