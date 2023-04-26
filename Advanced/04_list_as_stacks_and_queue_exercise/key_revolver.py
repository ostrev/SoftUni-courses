from collections import deque
price_bullet = int(input())
size_of_gun = int(input())
bullets = [int(s) for s in input().split()]
locks = [int(s) for s in input().split()]
intelligent = int(input())
all_bullet = len(bullets)
locks = deque(locks)
bullets_in_gun = deque()
is_reload = False
while bullets or bullets_in_gun:
    if not bullets_in_gun:
        is_reload = True
        if len(bullets) < size_of_gun:
            for _ in range(len(bullets)):
                bullets_in_gun.append(bullets.pop())
        else:
            for _ in range(size_of_gun):
                bullets_in_gun.append(bullets.pop())  # ako ostane edin patron
    if bullets_in_gun.popleft() <= locks[0]:
        print('Bang!')
        locks.popleft()
    else:
        print('Ping!')
    if is_reload and not bullets_in_gun and bullets:
        is_reload = False
        print('Reloading!')
    if not locks:
        bullets_left = len(bullets) + len(bullets_in_gun)
        money_earned = intelligent - ((all_bullet - bullets_left) * price_bullet)
        print(f"{bullets_left} bullets left. Earned ${money_earned}")
        break
    if not bullets_in_gun and not bullets:
        print(f"Couldn't get through. Locks left: {len(locks)}")

#******************************
from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])

intelligence = int(input())
used_bullets = 0

while locks and bullets:
    bullet = bullets.pop()
    lock = locks[0]

    used_bullets += 1

    if lock >= bullet:
        locks.popleft()
        print('Bang!')
    else:
        print('Ping!')

    if used_bullets % barrel_size == 0 and bullets:
        print('Reloading!')

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${intelligence - used_bullets * bullet_price}")