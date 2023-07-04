command = input()
meal_dic = {}
count = 0
while command != 'Stop':
    data = command.split('-')
    if data[0] == 'Like':
        guest = data[1]
        meal = data[2]
        if guest not in meal_dic:
            meal_dic[guest] = []
        if meal not in meal_dic[guest]:
            meal_dic[guest].append(meal)
    elif data[0] == 'Unlike':
        guest = data[1]
        meal = data[2]
        if guest not in meal_dic:
            print(f'{guest} is not at the party.')
        elif meal not in meal_dic[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            meal_dic[guest].remove(meal)
            count += 1
            print(f"{guest} doesn't like the {meal}.")

    command = input()

sort_dic = sorted(meal_dic.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))

for k, v in sort_dic:

    print(f"{k}: {', '.join(v)}")
print(f"Unliked meals: {count}")