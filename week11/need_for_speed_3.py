class Garage:
    def __init__(self):
        self.all_cars = []

    def add_car_to_garage(self, car_to_add, mileage_of_car, fuel_of_car):
        self.all_cars.append(Car(car_to_add, mileage_of_car, fuel_of_car))

    def print_garage(self):
        for car_to_show in self.all_cars:
            print(f'{car_to_show.name} -> Mileage: {car_to_show.car_mileage} kms, '
                  f'Fuel in the tank: {car_to_show.amount_fuel} lt.')

    def take_car(self, car_to_take, action, distance=0, fuel_amt=0):
        for element in self.all_cars:
            if element.name == car_to_take:
                if action == 'Drive':
                    element.drive_car(distance, fuel_amt)
                    if element.car_mileage >= 100000:
                        print(f'Time to sell the {element.name}!')
                        self.sell_car(element.name)
                elif action == 'Refuel':
                    element.refuel(fuel_amt)
                elif action == 'Revert':
                    element.revert_car(distance)

    def sell_car(self, car_to_sell):
        i = 0
        for element in self.all_cars:
            if element.name == car_to_sell:
                self.all_cars.pop(i)
            i += 1


class Car:
    def __init__(self, name, car_mileage, amount_fuel):
        self.name = name
        self.car_mileage = int(car_mileage)
        self.amount_fuel = int(amount_fuel)

    def drive_car(self, distance_to_drive: int, fuel_to_consume: int):
        if fuel_to_consume > self.amount_fuel:
            print('Not enough fuel to make that ride')
        else:
            self.car_mileage += distance_to_drive
            self.amount_fuel -= fuel_to_consume
            print(f'{self.name} driven for {distance_to_drive} kilometers. {fuel_to_consume} liters of fuel consumed.')

    def refuel(self, fuel_amount):
        amount_refueled = 0
        if self.amount_fuel + fuel_amount < 75:
            self.amount_fuel += fuel_amount
            amount_refueled = fuel_amount
        elif self.amount_fuel + fuel_amount >= 75:
            amount_refueled = 75 - self.amount_fuel
            self.amount_fuel = 75
        print(f'{self.name} refueled with {amount_refueled} liters')

    def revert_car(self, distance_to_revert):
        if self.car_mileage - distance_to_revert < 10000:
            self.car_mileage = 10000
        else:
            self.car_mileage -= distance_to_revert
            print(f'{self.name} mileage decreased by {distance_to_revert} kilometers')


number_of_cars = int(input())
car_garage = Garage()

for _ in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    car_garage.add_car_to_garage(car, mileage, fuel)

while True:
    command = input()
    if command == 'Stop':
        break
    command = command.split(' : ')
    if command[0] == 'Drive':
        car_name, distance_driven, fuel_consumed = command[1], int(command[2]), int(command[3])
        car_garage.take_car(car_name, command[0], distance=distance_driven,  fuel_amt=fuel_consumed)
    elif command[0] == 'Refuel':
        car_name, amount_refuel = command[1], int(command[2])
        car_garage.take_car(car_name, command[0], fuel_amt=amount_refuel)
    elif command[0] == 'Revert':
        car_name, distance_reverted = command[1], int(command[2])
        car_garage.take_car(car_name, command[0], distance=distance_reverted)

car_garage.print_garage()
