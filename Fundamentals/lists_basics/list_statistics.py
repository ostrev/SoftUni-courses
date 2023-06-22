number_of_integers = int(input())
positive_list = []
negative_list = []

for _ in range(number_of_integers):
    value = int(input())
    if value < 0:
        negative_list.append(value)
    else:
        positive_list.append(value)
print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}")
print(f'Sum of negatives: {sum(negative_list)}')
