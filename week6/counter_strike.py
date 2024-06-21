energy = int(input())
distance = input()
won = 0
lost = False

while distance != 'End of battle':
    if energy - int(distance) < 0:
        print(f'Not enough energy! Game ends with {won} won battles and {energy} energy')
        lost = True
        break
    energy -= int(distance)
    won += 1
    if won % 3 == 0:
        energy += won
    distance = input()

if not lost:
    print(f'Won battles: {won}. Energy left: {energy}')
