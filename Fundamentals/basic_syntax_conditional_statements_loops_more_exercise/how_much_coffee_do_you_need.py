text = input()

count_coffee = 0
my_list = ["dog", "cat", "movie", "coding", 'DOG', 'CAT', 'MOVIE', 'CODING']

while text != 'END':
    for operation in my_list:
        if operation in text:
            if text.isupper():
                count_coffee += 2

            if text.islower():
                count_coffee += 1
    text = input()
if count_coffee > 5:
    print('You need extra sleep')
else:
    print(count_coffee)

