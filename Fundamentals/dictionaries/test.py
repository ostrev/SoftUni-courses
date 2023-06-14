collection = {'Arnoldii': {'rarity': 4, 'rating': [], 'avg_rating': 0.0},
              'Woodii': {'rarity': 5, 'rating': [10, 5], 'avg_rating': 7.5},
              'Welwitschia': {'rarity': 2, 'rating': [7], 'avg_rating': 7.0}}

sorted_colletion = sorted(collection.items(), key=lambda kvp: (kvp[1]['rarity'], kvp[1]['avg_rating']))
print(sorted_colletion)