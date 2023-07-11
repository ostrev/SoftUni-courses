journal = input().split(', ')
command = input().split(' - ')
item_old = []
while command[0] != 'Craft!':
    item = command[1]

    if command[0] == 'Collect':
        if item not in journal:
            journal.append(item)
    elif command[0] == 'Drop':
        if item in journal:
            journal.remove(item)
    elif command[0] == 'Combine Items':
        item_old = item.split(':')
        if item_old[0] in journal:
            journal.insert(journal.index(item_old[0]) + 1, item_old[1])
    elif command[0] == 'Renew':
        if item in journal:
            journal.remove(item)
            journal.append(item)

    command = input().split(' - ')
print(', '.join(journal))
