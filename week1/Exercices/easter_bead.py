recipe_eggs = 1
recipe_flour = 1
recipe_milk = 0.25

budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price + (flour_price * 0.25)
milk_price_per_bread = milk_price / 4

bread_number = 0
eggs_nb = 0

while budget - (flour_price + eggs_price + milk_price_per_bread) > 0:
    budget -= (flour_price + eggs_price + milk_price_per_bread)
    bread_number += 1
    eggs_nb += 3
    if bread_number % 3 == 0:
        eggs_nb -= (bread_number - 2)

print(f'You made {bread_number} loaves of Easter bread! Now you have {eggs_nb} eggs and {budget:.2f}BGN left.')
