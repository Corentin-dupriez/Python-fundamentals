length = int(input())

nb_list = [input() for i in range(length)]

command = input()

new_list = [int(nb) for nb in nb_list if (command == 'even' and int(nb) % 2 == 0 or nb == 0)
            or (command == 'positive' and int(nb) >= 0)
            or (command == 'negative' and int(nb) < 0)
            or (command == 'odd' and int(nb) % 2 != 0)]

print(new_list)
