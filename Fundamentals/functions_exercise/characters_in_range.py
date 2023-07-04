def char_in_range(start, stop):
    one = ord(start)
    two = ord(stop)
    result = ''
    for i in range(one + 1, two):
        result += chr(i) + " "
    return result


start_string = input()
stop_string = input()
print(char_in_range(start_string, stop_string))
