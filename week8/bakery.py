list_items = input().split()
inventory = {}

for i in range(1, len(list_items)+1, 2):
    item = list_items[i-1]
    quantity = int(list_items[i])
    inventory[item] = quantity

print(inventory)
