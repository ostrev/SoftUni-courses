def orders(string, num):
    if string == 'coffee':
        result = num * 1.5
        return result
    elif string == 'coke':
        result = num * 1.4
        return result
    elif string == 'water':
        result = num * 1.0
        return result
    elif string == 'snacks':
        result = num * 2.0
        return result


command = input()
quantity = int(input())
print(f'{orders(command, quantity):.2f}')
