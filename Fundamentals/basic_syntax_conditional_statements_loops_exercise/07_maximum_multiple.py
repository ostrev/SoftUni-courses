divisor = int(input())
bound = int(input())

for i in range(bound, divisor, -1):
    if i % divisor == 0:
        print(i)
        break
