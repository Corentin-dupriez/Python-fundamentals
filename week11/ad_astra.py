import re


class FoodItem:

    def __init__(self, name, expiration_date, calories):
        self.name = name
        self.expiration_date = expiration_date
        self.calories = calories


pattern = r'(#|\|)(?P<food_item>[a-zA-Z\s]+)\1(?P<expiration_date>[0-9]{2}/[0-9]{2}/[0-9]{2})\1(?P<calories>\d{1,4})\1'

food_items = input()

matches = re.findall(pattern, food_items)
all_food = []
all_calories = 0

for item in matches:
    item_name = item[1]
    date = item[2]
    cal = int(item[3])
    all_food.append(FoodItem(item_name, date, cal))
    all_calories += cal

print(f'You have food to last you for: {all_calories // 2000} days!')
for food in all_food:
    print(f'Item: {food.name}, Best before: {food.expiration_date}, Nutrition: {food.calories}')
