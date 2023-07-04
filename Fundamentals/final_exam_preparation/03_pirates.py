def plunder(cities, town, people, gold):
    cities[town]['population'] -= people
    cities[town]['gold'] -= gold
    print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
    if cities[town]['population'] <= 0 or cities[town]['gold'] <= 0:
        del cities[town]
        print(f'{town} has been wiped off the map!')
    return


def prosper(cities, town, gold):
    if gold > 0:
        cities[town]['gold'] += gold
        print(f'{gold} gold added to the city treasury. {town} now has {cities[town]["gold"]} gold.')
    else:
        print("Gold added cannot be a negative number!")
        return
    return


command = input()
cities = {}
while command != 'Sail':
    data = command.split('||')
    city = data[0]
    population = int(data[1])
    gold = int(data[2])
    if city not in cities:
        cities[city] = {}
        cities[city]['population'] = population
        cities[city]['gold'] = gold
    else:
        cities[city]['population'] += population
        cities[city]['gold'] += gold
    command = input()

line = input()

while line != 'End':
    data_l = line.split('=>')
    if data_l[0] == 'Plunder':
        town = data_l[1]
        people = int(data_l[2])
        gold = int(data_l[3])
        plunder(cities, town, people, gold)
    elif data_l[0] == 'Prosper':
        town = data_l[1]
        gold = int(data_l[2])
        prosper(cities, town, gold)

    line = input()
sort_cities = sorted(cities.items(), key=lambda kvpt: (-kvpt[1]['gold'], kvpt[0]))
print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
for town, value in sort_cities:
    print(f'{town} -> Population: {value["population"]} citizens, Gold: {value["gold"]} kg')
