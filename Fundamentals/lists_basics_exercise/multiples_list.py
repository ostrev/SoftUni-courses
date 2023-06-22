factor = int(input())
count = int(input())
multiples = []

for i in range(1, count+1):
    element = i * factor
    multiples.append(element)
print(multiples)