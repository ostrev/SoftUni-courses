quantity = int(input())
days = int(input())

christmas_spirit = 0
total_cost = 0
last_day = False
for day in range(1, days + 1):
    last_day = False
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_cost += (2 * quantity)
        christmas_spirit += 5
    if day % 3 == 0:
        total_cost += ((5 * quantity) + (3 * quantity))
        christmas_spirit += 13
    if day % 5 == 0:
        total_cost += (15 * quantity)
        christmas_spirit += 17
        if day % 5 == 0 and day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        total_cost += 23
        christmas_spirit -= 20
        last_day = True
if last_day:
    christmas_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {christmas_spirit}")
