# string_manipulator
text = input()

command = input()
while command != 'End':
    data = command.split()

    if data[0] == 'Translate':
        char = data[1]
        replacement = data[2]
        text = text.replace(char, replacement)
        print(text)
    elif data[0] == 'Includes':
        substring = data[1]
        if substring in text:
            print(True)
        else:
            print(False)
    elif data[0] == 'Start':
        substring = data[1]
        print(text.startswith(substring))
    elif data[0] == 'Lowercase':
        text = text.lower()
        print(text)
    elif data[0] == 'FindIndex':
        char = data[1]
        print(text.rfind(char))
    elif data[0] == 'Remove':
        start_index = int(data[1])
        count = int(data[2])
        text = text[:start_index] + text[start_index + count:]
        print(text)

    command = input()