def stock_availability(*args):
    cupcakes = args[0]
    command = args[1]
    if command == 'delivery':
        for i in args[2:]:
            cupcakes.append(i)
    elif command == 'sell':
        if len(args) == 2:
            cupcakes.pop(0)
        elif len(args) > 2:
            if str(args[2]).isdigit():
                param = args[2]
                for i in range(param):
                    if cupcakes:
                        cupcakes.pop(0)
            else:
                lst = args[2:]
                for item in lst:
                    for i in range(len(cupcakes)):
                        if cupcakes[i] == item:
                            cupcakes[i] = ''
    return [i for i in cupcakes if i != '']


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))


# print(stock_availability(["chocolate", "vanilla", "banana"],
#                          "sell", "cookie", "banana"))
