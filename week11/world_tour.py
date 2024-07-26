def insert_stop(index: int, stop_name: str, list_stops: str) -> str:
    return list_stops[:index] + stop_name + list_stops[index:]


def remove_stop(index_start: int, index_end: int, list_stops: str) -> str:
    return list_stops[:index_start] + list_stops[index_end + 1:]


def switch_destination(old_destination: str, new_destination: str, list_stops: str) -> str:
    while old_destination in list_stops:
        index_start = list_stops.index(old_destination)
        index_end = index_start + len(old_destination)
        list_stops = list_stops[:index_start] + new_destination + list_stops[index_end:]
    return list_stops


stops = input()

while True:
    command = input()
    if command == 'Travel':
        break
    command = command.split(':')
    if command[0] == 'Add Stop':
        index_to_insert, stop_to_insert = int(command[1]), command[2]
        stops = insert_stop(index_to_insert, stop_to_insert, stops)
        print(stops)
    elif command[0] == 'Remove Stop':
        index_to_start, index_to_end = int(command[1]), int(command[2])
        stops = remove_stop(index_to_start, index_to_end, stops)
        print(stops)
    elif command[0] == 'Switch':
        old_dest, new_dest = command[1], command[2]
        stops = switch_destination(old_dest, new_dest, stops)
        print(stops)

print(f'Ready for world tour! Planned stops: {stops}')
