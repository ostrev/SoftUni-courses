numbers = input().split(', ')
numbers = list(map(int, numbers))
result = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        result.append(i)
print(result)

# numbers = list(map(int, input().split(", ")))
# even_indices = []
#
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         even_indices.append(i)
#
# print(even_indices)
