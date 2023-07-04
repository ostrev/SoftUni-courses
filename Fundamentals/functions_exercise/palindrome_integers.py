def palindrome(num):
    counter = 0
    res = []
    for element in numbers:
        for index in range(0, len(element) // 2):
            if element[index] == element[((len(element)-1) - index)]:
                counter += 1
        if counter == len(element) // 2:
            counter = 0
            res.append(True)
        else:
            res.append(False)
    return res


numbers = input().split(', ')
for i in palindrome(numbers):
    print(i)
print(*palindrome(numbers), sep="\n") # print wmesto for

    # res = str(element) == str(element)[::-1]
    # print(res)