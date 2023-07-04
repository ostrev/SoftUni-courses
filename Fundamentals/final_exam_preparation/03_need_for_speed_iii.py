def drive(cars, car, distance, fuel):
    if cars[car]['fuel'] < fuel:
        print('Not enough fuel to make that ride')
    else:
        cars[car]['fuel'] -= fuel
        cars[car]['mileage'] += distance
        print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
    if cars[car]['mileage'] >= 100000:
        del cars[car]
        print(f'Time to sell the {car}!')
    return


def refuel(cars, car, fuel):
    if cars[car]['fuel'] >= 75:
        print(f'{car} refueled with {0} liters')
    else:
        if cars[car]['fuel'] + fuel > 75:
            left = abs(fuel - ((cars[car]['fuel'] + fuel) - 75))
            cars[car]['fuel'] = 75
            print(f'{car} refueled with {left} liters')
        else:
            cars[car]['fuel'] += fuel
            print(f'{car} refueled with {fuel} liters')
    return


def revert(cars, car, kilo):
    cars[car]['mileage'] -= kilo
    if cars[car]['mileage'] < 10000:
        cars[car]['mileage'] = 10000
    else:
        print(f'{car} mileage decreased by {kilo} kilometers')
    return


number_of_cars = int(input())
cars = {}
for _ in range(number_of_cars):
    data = input().split('|')
    car_name = data[0]
    mileage = int(data[1])
    fuel = int(data[2])
    cars[car_name] = {}
    cars[car_name]['mileage'] = mileage
    cars[car_name]['fuel'] = fuel

command = input()

while command != 'Stop':
    data = command.split(' : ')
    if data[0] == 'Drive':
        car = data[1]
        distance = int(data[2])
        fuel = int(data[3])
        drive(cars, car, distance, fuel)
    elif data[0] == 'Refuel':
        car = data[1]
        fuel = int(data[2])
        refuel(cars, car, fuel)
    elif data[0] == 'Revert':
        car = data[1]
        kilo = int(data[2])
        revert(cars, car, kilo)

    command = input()

sort_cars = sorted(cars.items(), key=lambda kvpt: (-kvpt[1]['mileage'], kvpt[0]))
# print(sort_cars)
for k, v in sort_cars:
    print(f"{k} -> Mileage: {v['mileage']} kms, Fuel in the tank: {v['fuel']} lt.")
