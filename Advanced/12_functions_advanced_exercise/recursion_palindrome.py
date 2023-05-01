def palindrome(text, index):
    if len(text) // 2 == index:
        return f'{text} is a palindrome'
    left = text[index]
    right = text[len(text) - 1 - index]
    if left != right:
        return f'{text} is not a palindrome'
    return palindrome(text, index + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
