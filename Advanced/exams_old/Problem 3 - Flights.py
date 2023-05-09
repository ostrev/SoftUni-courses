def flights(*args):
    destinations = []
    passengers = []
    result = {}

    for i in range(len(args)):
        if args[i] == 'Finish':
            break
        if i % 2 == 0:
            destinations.append(args[i])
        else:
            passengers.append(args[i])

    for index in range(len(destinations)):
        if destinations[index] not in result:
            result[destinations[index]] = 0
        result[destinations[index]] += passengers[index]

    return result

print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
