data = [int(s) for s in input().split()]
average = sum(data)/len(data)
greater = []
for number in data:
    if number > average:
        greater.append(number)
result = sorted(greater, reverse=True)
range_result = 0
output = []
if not greater:
    print("No")
else:
    if len(result) >= 5:
        range_result = 5
    else:
        range_result = len(result)
    for num in range(range_result):
        output.append(result[num])
    print(*output)
