import math

n = int(input())
capacity = int(input())

courses = (n / capacity)
courses = math.ceil(courses)
print(courses)