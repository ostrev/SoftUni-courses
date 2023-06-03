sheep_str = input().split(", ")

if sheep_str.pop() == 'wolf':
    print("Please go away and stop eating my sheep")

sheep_str_rev = sheep_str[::-1]
for i in range(len(sheep_str_rev)):
    if sheep_str_rev[i] != 'sheep':
        print(f"Oi! Sheep number {i + 1}! You are about to be eaten by a wolf!")
