from os import listdir, path


def traverse_dir(current_path, files_by_ext):
    for element in listdir(current_path):
        if path.isdir(path.join(current_path, element)):
            traverse_dir(path.join(current_path, element), files_by_ext)
        else:
            extension = element.split('.')[-1]
            if extension not in files_by_ext:
                files_by_ext[extension] = []
            files_by_ext[extension].append(element)


files_by_ext = {}
traverse_dir('.', files_by_ext)


for ext, files in files_by_ext.items():
    print(f".{ext}")
    for file in files:
        print(f"--- {file}")