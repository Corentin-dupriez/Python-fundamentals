times = input().split(' ')

time_left = times[:int(len(times)/2)]
time_right = times[int(len(times)/2)+1:]

time_right.reverse()

calculate_time_left = 0
calculate_time_right = 0

for i in time_left:
    if int(i) == 0:
        calculate_time_left = calculate_time_left * 0.8
    else:
        calculate_time_left += int(i)

for i in time_right:
    if int(i) == 0:
        calculate_time_right = calculate_time_right * 0.8
    else:
        calculate_time_right += int(i)

if calculate_time_left < calculate_time_right:
    print(f'The winner is left with total time: {calculate_time_left:.1f}')
else:
    print(f'The winner is right with total time: {calculate_time_right:.1f}')
