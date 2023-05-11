def start_spring(**kwargs):
    res = {}
    for k, v in kwargs.items():
        if v not in res:
            res[v] = []
        res[v].append(k)

    result_d = sorted(res.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    result = ""
    new_list = []
    for key, value in result_d:
        new_list = []
        value = sorted(value)
        for i in value:
            new = f'-' + i
            new_list.append(new)

        vel = "\n". join(new_list)
        result += f'{key}:\n' \
               f'{vel}' \
                f'\n'

    return result




example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

# *******************
def start_spring(**kwargs):
    collection_objects = {}
    for objects, type in kwargs.items():
        if type not in collection_objects:
            collection_objects[type] = [objects]
        else:
            collection_objects[type].append(objects)

    collection_objects = {x: sorted(collection_objects[x]) for x in collection_objects.keys()}
    sorted_collection = sorted(collection_objects.items(), key=lambda pair: (-(len(pair[1])), pair[0]))
    result = ''
    for type, objects in sorted_collection:
        result += f'{type}:\n'
        for object in objects:
            result += f'-{object}\n'
    return result.rstrip()