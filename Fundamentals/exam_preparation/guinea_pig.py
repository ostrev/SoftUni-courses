food_quantity = float(input()) * 1000
hay_quantity = float(input()) * 1000
cover_quantity = float(input()) * 1000
weight = float(input()) * 1000
day_count = 0
while day_count < 30:
    day_count += 1
    food_quantity -= 300
    if day_count % 2 == 0:
        hay_quantity = hay_quantity - (food_quantity * 0.05)
    if day_count % 3 == 0:
        cover_quantity = cover_quantity - (weight / 3)

if food_quantity > 0 and hay_quantity > 0 and cover_quantity > 0:
    print(f"Everything is fine! Puppy is happy! Food: {food_quantity/1000:.2f}, Hay: {hay_quantity/1000:.2f}, Cover: {cover_quantity/1000:.2f}.")
else:
    print("Merry must go to the pet store!")
