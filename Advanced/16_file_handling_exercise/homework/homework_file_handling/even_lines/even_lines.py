symbols_to_replace = ["-", ",", ".", "!", "?"]
with open('text.txt') as file:
    text = file.readlines()
    for index in range(len(text)):
        if index % 2 == 0:
            current_string = text[index].strip()
            for symbol in symbols_to_replace:
                current_string = current_string.replace(symbol, '@')
            string_as_list = current_string.split()[::-1]
            print(' '.join(string_as_list))
