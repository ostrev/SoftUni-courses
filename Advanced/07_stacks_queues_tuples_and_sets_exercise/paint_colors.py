from collections import deque

colors = deque(input().split())

main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]
find_colors = []

is_last = False
while colors:
    if len(colors) == 1:
        last_string = ''
        is_last = True
    else:
        last_string = colors.pop()

    first_string = colors.popleft()
    result = first_string + last_string
    result_rev = last_string + first_string
    if result in main_colors or result in secondary_colors:
        find_colors.append(result)
    elif result_rev in main_colors or result_rev in secondary_colors:
        find_colors.append(result_rev)
    else:
        if len(first_string) > 1:
            first_string = first_string[:-1]
            pos = len(colors) // 2
            colors.insert(pos, first_string)
        if len(secondary_colors) > 1 and is_last == False:
            last_string = last_string[:-1]
            pos = len(colors) // 2
            colors.insert(pos, last_string)
last_colors = []
for color in find_colors:
    if color == "orange":
        if "red" in find_colors and "yellow" in find_colors:
            last_colors.append(color)
    elif color ==  "purple":
        if "red" in find_colors and "blue" in find_colors:
            last_colors.append(color)
    elif color == "green":
        if "blue" in find_colors and "yellow" in find_colors:
            last_colors.append(color)
    else:
        last_colors.append(color)


print(last_colors)