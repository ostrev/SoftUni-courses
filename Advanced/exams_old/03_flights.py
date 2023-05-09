def flights(*args):
    flights = {}
    destination = [i for i in args[:args.index('Finish')] if not str(i).isdigit()]
    passengers = [int(i) for i in args[:args.index('Finish')] if str(i).isdigit()]
    for i, j in zip(destination, passengers):
        if i not in flights:
            flights[i] = j
        else:
            flights[i] += j
    return flights




# print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

# print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
# print(flights('London', 0, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

# print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))