import math

party_size = int(input())
days = int(input())
companions_count = party_size
coins = 0

for i in range(1, days + 1):
    if i % 10 == 0:
        companions_count -= 2
    if i % 15 == 0:
        companions_count += 5
    if i % 1 == 0:
        coins += 50 - (companions_count * 2)
    if i % 3 == 0:
        coins -= (3 * companions_count)
    if i % 5 == 0:
        coins += (20 * companions_count)
        if i % 3 == 0:
            coins -= (2 * companions_count)




print(f"{companions_count} companions received {math.trunc(coins/companions_count)} coins each.")
