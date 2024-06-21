numbers = input()
nb_list = numbers.split(' ')

for nb in range(len(nb_list)):
    nb_list[nb] = -int(nb_list[nb])

print(nb_list)
