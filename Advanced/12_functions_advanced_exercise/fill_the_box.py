def fill_the_box(hight, length, width, *args):
    volume = hight * length * width
    cubs_left = 0
    for element in args:
        if element == 'Finish':
            break
        if element > volume:
            element -= volume
            cubs_left += element
            volume = 0
        else:
            volume -= element

    if volume > 0:
        return f'There is free space in the box. You could put {volume} more cubes.'
    else:
        return f'No more free space! You have {cubs_left} more cubes.'


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
