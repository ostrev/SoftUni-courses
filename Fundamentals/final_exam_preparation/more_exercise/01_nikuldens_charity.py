def index_check(text, start, end):
    if start < 0 or end < 0:
        print('Invalid indexes!')
        return True
    else:
        if start > len(text) - 1:
            print('Invalid indexes!')
            return True
        elif end > len(text) - 1:
            print('Invalid indexes!')
            return True
        return False


text = input()

command = input()

while command != 'Finish':
    data = command.split()
    if data[0] == 'Replace':
        current_char = data[1]
        new_char = data[2]
        text = text.replace(current_char, new_char)  # check if char is in text
        print(f"{text}")
    elif data[0] == 'Cut':
        start = int(data[1])
        end = int(data[2])
        if not index_check(text, start, end):
            text = text[:start] + text[end+1:]
            print(f'{text}')
    elif data[0] == 'Make':
        if data[1] == 'Upper':
            text = text.upper()
            print(text)
        else:
            text = text.lower()
            print(text)
    elif data[0] == 'Check':
        ch_string = data[1]
        if ch_string in text:
            print(f'Message contains {ch_string}')
        else:
            print(f"Message doesn't contain {ch_string}")
    elif data[0] == 'Sum':
        start = int(data[1])
        end = int(data[2])
        if not index_check(text, start, end):
            substring = text[start:end + 1]
            chars_sum = 0
            for char in substring:
                chars_sum += ord(char)
            print(chars_sum)
    command = input()
