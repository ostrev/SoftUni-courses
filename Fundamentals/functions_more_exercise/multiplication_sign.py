def sign(number_one, number_two, number_three):
    result = ''
    if number_one == 0 or number_two == 0 or number_three == 0:
        result = 'zero'
        return result
    elif number_one > 0 and number_two > 0 and number_three > 0:
        result = 'positive'
        return result
    elif number_one < 0 and number_two < 0 and number_three < 0:
        result = 'negative'
        return result
    elif number_one < 0 and number_two < 0 and number_three > 0:
        result = 'positive'
        return result
    elif number_one > 0 and number_two < 0 and number_three < 0:
        result = 'positive'
        return result
    elif number_one < 0 and number_two > 0 and number_three < 0:
        result = 'positive'
        return result
    else:
        result = 'negative'
        return result


one = int(input())
two = int(input())
three = int(input())
print(sign(one, two, three))