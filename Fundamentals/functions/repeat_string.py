def string_repeat(string, num):
    result = string * num
    return result


initial_string = input()
counter = int(input())
print(string_repeat(initial_string, counter))
