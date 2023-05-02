numbers_dictionary = {}
command = input()

while command != "Search":
    number_as_string = command
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")
    command = input()

command = input()
while not command == "Remove":
    searched = command
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in the dictionary")
    command = input()

command = input()
while not command == "End":
    searched = command
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in the dictionary")
    command = input()

print(numbers_dictionary)