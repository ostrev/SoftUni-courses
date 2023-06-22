permutation = input().split()

step = int(input())
counter = 0
reset_index = 0
result = []

while len(permutation) > 0:
    counter += 1
    if counter % step == 0:
        result.append(permutation.pop(reset_index))
    else:
        reset_index += 1

    if len(permutation) == reset_index:
        reset_index = 0

print(f"[{','.join(result)}]")
