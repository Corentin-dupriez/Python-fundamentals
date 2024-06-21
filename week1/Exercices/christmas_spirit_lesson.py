quantity_decorations = int(input())
remaining_days = int(input())

total_cost = 0
total_spirit = 0

ornament_set_price = 2
ornament_set_spirit = 5
skirt_price = 5
skirt_spirit = 3
garland_price = 3
garland_spirit = 10
lights_price = 15
lights_spirit = 17

for current_day in range(1, remaining_days + 1):
    if current_day % 11 == 0:
        quantity_decorations += 2
    if current_day % 2 == 0:
        total_cost += ornament_set_price * quantity_decorations
        total_spirit += ornament_set_spirit
    if current_day % 3 == 0:
        total_cost += (skirt_price + garland_price) * quantity_decorations
        total_spirit += skirt_spirit + garland_spirit
    if current_day % 5 == 0:
        total_cost += lights_price * quantity_decorations
        total_spirit += lights_spirit
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_spirit -= 20
        total_cost += skirt_price + garland_price + lights_price

