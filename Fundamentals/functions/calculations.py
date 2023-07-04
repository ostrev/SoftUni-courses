def calc_operators(operator, first, second):
    if operator == 'multiply':
        result = first * second
        return result
    elif operator == 'divide':
        result = first // second
        return result
    elif operator == 'add':
        result = first + second
        return result
    elif operator == 'subtract':
        result = first - second
        return result


command = input()
numb_one = int(input())
numb_two = int(input())

print(calc_operators(command, numb_one, numb_two))
