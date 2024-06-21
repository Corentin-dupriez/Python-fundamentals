lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
repair_cost = 0

for lost_fight in range(1, lost_fights + 1):
    if lost_fight % 2 == 0:
        repair_cost += helmet_price
        if lost_fight % 3 == 0:
            repair_cost += shield_price
        if lost_fight % 12 == 0:
            repair_cost += armor_price
    if lost_fight % 3 == 0:
        repair_cost += sword_price

print(f'Gladiator expenses: {repair_cost:.2f} aureus')
