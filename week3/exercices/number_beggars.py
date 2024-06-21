money = input().split(', ')
nb_beggars = int(input())
collected = []

for beggar in range(nb_beggars):
    collected_by_beggar = []
    for i in range(beggar, len(money), nb_beggars):
        collected_by_beggar.append((int(money[i])))
    collected.append(sum(collected_by_beggar))

print(collected)
