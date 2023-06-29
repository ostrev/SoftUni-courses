version = [int(s) for s in input().split('.')]
version[-1] += 1

for i in range(len(version) - 1, - 1, - 1):
    if version[i] > 9:
        version[i] = 0
        version[i - 1] += 1
version = list(map(str, version))

print('.'.join(version))

