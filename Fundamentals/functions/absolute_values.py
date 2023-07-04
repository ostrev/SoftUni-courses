def abs_number():
    result = list(map(float, numbers))
    result = [abs(i) for i in result]
    return result


numbers = input().split()
print(abs_number())
