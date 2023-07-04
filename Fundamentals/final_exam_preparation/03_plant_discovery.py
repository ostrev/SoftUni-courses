def check_name(plants, plant):
    if plant not in plants:
        print('error')
        return True
    return False


numbers = int(input())

plants = {}
for _ in range(numbers):
    info = input().split('<->')
    plant = info[0]
    rarity = int(info[1])
    plants[plant] = {}
    plants[plant]['rarity'] = rarity



command = input()

while command != 'Exhibition':
    data = command.split(': ')
    if data[0] == 'Rate':
        data_s = data[1].split(' - ')
        plant = data_s[0]
        rating = int(data_s[1])
        if check_name(plants, plant):
            command = input()
            continue
        if 'rating' not in plants[plant]:
            plants[plant]['rating'] = []
        plants[plant]['rating'].append(rating)

    elif data[0] == 'Update':
        data_s = data[1].split(' - ')
        plant = data_s[0]
        new_rarity = int(data_s[1])
        if check_name(plants, plant):
            command = input()
            continue
        plants[plant]['rarity'] = new_rarity
    elif data[0] == 'Reset':
        data_s = data[1].split(' - ')
        plant = data_s[0]
        if check_name(plants, plant):
            command = input()
            continue
        plants[plant]['rating'].clear()
                                        # ako dobadq 0 na reitinga move da ne otchita vqrno avr
    command = input()

for k in plants:
    if 'rating' not in plants[k]:
        plants[k]['rating'] = [0]
    if not plants[k]['rating']:
        plants[k]['rating'] = [0]
    a = plants[k]['rating']
    avr = sum(a)/len(a)
    plants[k]['rating'] = avr

sort_plants = sorted(plants.items(), key=lambda kvpt: (-kvpt[1]['rarity'], -kvpt[1]['rating']))
print('Plants for the exhibition:')
for k, v in sort_plants:
    print(f'- {k}; Rarity: {v["rarity"]}; Rating: {v["rating"]:.2f}')

