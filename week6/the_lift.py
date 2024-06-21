people = int(input())
lift = input().split()
filled_lift = list()

for wagon in lift:
    filled_wagon = int(wagon)
    while people > 0 and filled_wagon < 4:
        people -= 1
        filled_wagon += 1
    filled_lift.append(str(filled_wagon))

if people == 0:
    if int(min(filled_lift)) < 4:
        print('The lift has empty spots!')
else:
    if people > 0:
        print(f'There isn\'t enough space! {people} people in a queue!')
print(' '.join(filled_lift))
