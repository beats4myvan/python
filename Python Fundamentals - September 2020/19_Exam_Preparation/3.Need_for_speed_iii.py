n = int(input())
garage = {}
for _ in range(n):
    n_cars = input().split("|")
    cars, mileage, fuel = n_cars
    garage[cars] = {'mileage': int(mileage), 'fuel': int(fuel)}


def drive(car, distance, fuel):
    if fuel > garage[car]['fuel']:
        print("Not enough fuel to make that ride")
    else:
        garage[car]['mileage'] += distance
        garage[car]['fuel'] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
    if garage[car]['mileage'] > 100000:
        print(f"Time to sell the {car}!")
        del garage[car]


def refuel(car, fuel):
    garage[car]['fuel'] += fuel
    if garage[car]['fuel'] > 75:
        to_fill = 75 + fuel - garage[car]['fuel']
        garage[car]['fuel'] = 75
        print(f'{car} refueled with {to_fill} liters')
    else:
        print(f"{car} refueled with {fuel} liters")

def revert(car, kilometers):
    garage[car]["mileage"] -= kilometers
    if not garage[car]['mileage'] < 10000:
        print(f"{car} mileage decreased by {kilometers} kilometers")
    if garage[car]['mileage'] < 10000:
        garage[cars]['mileage'] = 10000

command = input()
while command != "Stop":
    command = command.split(" : ")
    if command[0] == "Drive":
        drive(command[1], int(command[2]), int(command[3]))
    elif command[0] == "Refuel":
        refuel(command[1], int(command[2]))

    elif command[0] == "Revert":
        revert(command[1],int(command[2]))
    command = input()

sort_garage = sorted(garage.items(), key=lambda x: (-x[1]['mileage'], x[0]))

for key, value in sort_garage:
    print(f"{key} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")
