first_set = set([int(s) for s in input().split()])
second_set = set([int(s) for s in input().split()])
num = int(input())
temp_set = set()
for i in range(num):
    line = input()
    if 'Add First' in line:
        line = line.split()
        for el in range(2, len(line)):
            numb = line[el]
            first_set.add(int(numb))
    elif 'Add Second' in line:
        line = line.split()
        for el in range(2, len(line)):
            numb = line[el]
            second_set.add(int(numb))
    elif 'Check Subset' in line:
        print(first_set.issubset(second_set) or second_set.issubset(first_set))
    elif 'Remove First' in line:
        line = line.split()
        line = line[2::]
        line = [int(s) for s in line]
        line = set(line)
        first_set = first_set.difference(line)
    else:
        line = line.split()
        line = line[2::]
        line = [int(s) for s in line]
        line = set(line)
        second_set = second_set.difference(line)

print(*(sorted(first_set)), sep=", ")
print(*sorted(second_set), sep=", ")
