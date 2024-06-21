class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

    def get_info(self, species):
        if species == 'mammal':
            return f'Mammals in {self.name}: {", ".join(self.mammals)}\nTotal animals: {len(self.mammals) + len(self.birds) + len(self.fishes)}'
        elif species == 'fish':
            return f'Fishes in {self.name}: {", ".join(self.fishes)}\nTotal animals: {len(self.mammals) + len(self.birds) + len(self.fishes)}'
        elif species == 'bird':
            return f'Birds in {self.name}: {", ".join(self.birds)}\nTotal animals: {len(self.mammals) + len(self.birds) + len(self.fishes)}'


zoo = Zoo(input())
number_animals = int(input())

for _ in range(number_animals):
    animal_to_add = input().split()
    zoo.add_animals(animal_to_add[0], animal_to_add[1])

species_to_print = input()
print(zoo.get_info(species_to_print))
