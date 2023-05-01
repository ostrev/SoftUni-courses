def sum_of_numbers(numbers):
    return sum(numbers)


positive = []
negative = []
line = [int(s) for s in input().split()]
for num in line:
    if num < 0 :
        negative.append(num)
    else:
        positive.append(num)

print(sum_of_numbers(negative))
print(sum_of_numbers(positive))

if abs((sum_of_numbers(negative))) > sum_of_numbers(positive):
    print("The negatives are stronger than the positives")
if sum_of_numbers(positive) > abs((sum_of_numbers(negative))):
    print("The positives are stronger than the negatives")


