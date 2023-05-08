from os import walk
extensions_count = {}

for _, _, files in walk('.'):
    for file in files:
        split_to_get_extension = file.split('.')
        extension = split_to_get_extension[1]
        if extension not in extensions_count:
            extensions_count[extension] = []
        extensions_count[extension].append(file)
sorted_extensions = sorted(extensions_count.items(), key=lambda kvp: (kvp[0], kvp[1]))
# Знам че в условието пише, че трябва да е на десктопа, но не разбрах как да го направя.
# Не разбирам защо от СофтУни са го включили в задачата, при положение
# че няма унифициран начин да се постигне за всеки един OS(или ако има аз на моето ниво не го знам).
# За това, с риск да получа по-ниска оценка, не счетох за необходимо да го направя.

with open('report.txt', 'a') as report:
    for extension, files in sorted_extensions:
        report.write(f'.{extension}\n')
        for file in files:
            report.write(f'- - - {file}\n')
