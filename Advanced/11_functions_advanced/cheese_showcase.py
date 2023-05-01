def sorting_cheeses(**kwargs):
    result = ''
    sort_kwargs = sorted(kwargs.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    for k, v in sort_kwargs:
        result += k + '\n'
        sorted_cheese = sorted(v, reverse=True)
        result += '\n'.join([str(s) for s in sorted_cheese])
        result += '\n'
    return result
print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
