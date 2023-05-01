def age_assignment(*args, **kwargs):
    result = {}

    for k, v in kwargs.items():
        for name in args:
            if k in name:
                result[name] = v
    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
