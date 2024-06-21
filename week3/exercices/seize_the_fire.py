cell_and_fire = input().split('#')
water = int(input())
all_cells = list()
put_out_cells = list()
effort = 0
fire = 0

for cell in cell_and_fire:
    cells = cell.split(' = ')
    all_cells.append(cells)

for cell in all_cells:
    if (cell[0] == 'High' and int(cell[1]) in range(81, 126) \
            or cell[0] == 'Medium' and int(cell[1]) in range(51, 81) \
            or cell[0] == 'Low' and int(cell[1]) in range(1, 51)) and water >= int(cell[1]):
        water -= int(cell[1])
        put_out_cells.append(int(cell[1]))
        effort += int(cell[1]) * 0.25
        fire += int(cell[1])

print('Cells:')
for put_out_cell in put_out_cells:
    print(f' - {put_out_cell}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {fire}')
