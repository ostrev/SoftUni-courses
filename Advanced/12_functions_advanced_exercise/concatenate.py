def concatenate(*args):
    result = ''
    for ar in args:
        result += ar
    return result

print(concatenate("Soft", "Uni", "Is", "Great", "!"))
print(concatenate("I", " ", "Love", " ", "Python"))
