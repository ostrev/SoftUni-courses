from os import walk

files_by_ext = {}
for _, _, files in walk('.'):
    for file in files:
        extension = file.split('.')[-1]
        if extension not in files_by_ext:
            files_by_ext[extension] = []
        files_by_ext[extension].append(file)


for extension, files in sorted(files_by_ext.items()):
    print(f'.{extension}')
    for file in sorted(files):
        print(f'--- {file}')