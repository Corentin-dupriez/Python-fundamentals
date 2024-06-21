import math

efficiency = 0

for employee in range(3):
    efficiency += int(input())

nb_students = int(input())

time_no_break = math.ceil(nb_students / efficiency)

if time_no_break % 3 != 0:
    breaks = time_no_break // 3
else:
    breaks = 0

print(f'Time needed: {time_no_break + breaks}h.')
