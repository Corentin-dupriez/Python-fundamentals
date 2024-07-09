def print_capitals(capitals_dict: dict):
    for i, j in capitals_dict.items():
        print(f'{i} -> {j}')


cities = input().split(', ')
countries = input().split(', ')

capitals = dict(zip(cities, countries))

print_capitals(capitals)
