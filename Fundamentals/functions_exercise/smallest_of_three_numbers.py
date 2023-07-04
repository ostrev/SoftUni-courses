def smallest_of_three(a, b, c):
    result= []
    result.append(a)
    result.append(b)
    result.append(c)
    result = [min(result)]
    result = list(map(str, result))
    f = (''.join(result[0]))
    return f



first = int(input())
second = int(input())
third = int(input())

print(smallest_of_three(first, second, third))