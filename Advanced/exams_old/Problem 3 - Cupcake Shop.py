def stock_availability(boxes, command, *args):
    # list_inventory = dq(boxes)
    if command == 'delivery':
        for box in args:
            boxes.append(box)
    elif command == 'sell':
        if args and str(args[0]).isdigit(): # NUMBER
            num = int(args[0])
            for i in range(num):
                art = boxes[0]
                boxes.remove(art)
        elif args and not str(args[0]).isdigit(): # STRING
            for art in args:
                while art in boxes:
                    boxes.remove(art)
        else:
            art = boxes[0]
            boxes.remove(art)
    return boxes





print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate", "banana"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))




# Output
# ['choco', 'vanilla', 'banana', 'caramel', 'berry']
# ['chocolate', 'vanilla', 'banana', 'cookie', 'banana']
# ['vanilla', 'banana']
# []
# ['banana']
# ['cookie', 'banana']
# ['chocolate', 'vanilla', 'banana']
