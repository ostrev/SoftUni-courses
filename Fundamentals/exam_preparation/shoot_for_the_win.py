targets = [int(num) for num in input().split()]
command = input()
count_shoot = 0

while command != 'End':
    index = int(command)
    if 0 <= index < len(targets):
        current_target = targets[index]
        if targets[index] != -1:
            targets[index] = -1
            count_shoot += 1
        for digits in range(len(targets)):
            if targets[digits] != -1:
                if targets[digits] > current_target:
                    targets[digits] -= current_target
                else:
                    targets[digits] += current_target
    command = input()

print(f"Shot targets: {count_shoot} -> {' '.join(str(s) for s in targets)}")
