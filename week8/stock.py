def create_inventory(elements):
    inventory = {}
    for i in range(1, len(elements) + 1, 2):
        item = elements[i - 1]
        quantity = int(elements[i])
        inventory[item] = quantity
    return inventory


def check_items(item):
    if item in bakery.keys():
        return f'We have {bakery[item]} of {item} left'
    return f'Sorry, we don\'t have {item}'


list_items = input().split()
bakery = create_inventory(list_items)
customer_requests = input().split()
for element in customer_requests:
    print(check_items(element))
