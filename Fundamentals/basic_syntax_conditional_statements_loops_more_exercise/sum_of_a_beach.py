# text = input().lower()
#
# my_list = ["sand", "water", "fish", "sun"]
# counter = 0
#
# for item in my_list:
#     if item in text:
#         word_count_txt = text.count(item)
#         counter += word_count_txt
#
# print(counter)


DOG = 'dog'
CAT = 'cat'
OTHER = 'Other'

TYPES = [ x for x in (DOG, CAT, OTHER)]
max_length = max(len(x) for (x) in TYPES)
print(max_length)
print(TYPES)
