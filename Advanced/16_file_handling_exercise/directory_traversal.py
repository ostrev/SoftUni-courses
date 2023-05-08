
from os import walk, path

files_dic = {}
for _, _, files, in walk(input()):
    for file in files:
        extension = file.split('.')[-1]
        if extension not in files_dic:
            files_dic[extension] = []
        files_dic[extension].append(file)
with open(path.expanduser('~/Desktop/result.txt'), 'w') as output:
# with open('result.txt', 'w') as output:
    for key, value in sorted(files_dic.items()):
        output.write(f'.{key}\n')
        for i in sorted(value):
           output.write(f'- - - {i}\n')
