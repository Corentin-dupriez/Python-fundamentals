def find_path(start_row, start_col, array, already_visited=[]):
    visited = already_visited
    visited.append((start_row, start_col))
    near = [(start_row, start_col)]
    while len(near) > 0:
        if array[start_row][start_col] == 'e':
            return visited
        current_cell = near.pop()
        for direction in 'LRUD':
            if direction == 'L':
                new_cell = (current_cell[0], current_cell[1] - 1)
                if 0 < new_cell[0] < len(array) and 0 < new_cell[1] < len(array[0]):
                    if array[new_cell[0]][new_cell[1]] == '-' and new_cell not in visited:
                        find_path(new_cell[0], new_cell[1], array, visited)
            elif direction == 'R':
                new_cell = (current_cell[0], current_cell[1] + 1)
                if 0 < new_cell[0] < len(array) and 0 < new_cell[1] < len(array[0]):
                    if array[new_cell[0]][new_cell[1]] == '-' and new_cell not in visited:
                        find_path(new_cell[0], new_cell[1], array, visited)
            elif direction == 'U':
                new_cell = (current_cell[0] - 1, current_cell[1])
                if 0 < new_cell[0] < len(array) and 0 < new_cell[1] < len(array[0]):
                    if array[new_cell[0]][new_cell[1]] == '-' and new_cell not in visited:
                        find_path(new_cell[0], new_cell[1], array, visited)
            elif direction == 'D':
                new_cell = (current_cell[0] + 1, current_cell[1])
                if 0 < new_cell[0] < len(array) and 0 < new_cell[1] < len(array[0]):
                    if array[new_cell[0]][new_cell[1]] == '-' and new_cell not in visited:
                        find_path(new_cell[0], new_cell[1], array, visited)
        visited.append(new_cell)
        near.append(new_cell)
    return visited


rows_in_labyrinth = int(input())
labyrinth = []

for row_in_labyrinth in range(rows_in_labyrinth):
    labyrinth.append(input().split())

print(labyrinth)

print(find_path(0, 0, labyrinth))
