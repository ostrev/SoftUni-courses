words = [s for s in input().split()]
palindrome = input()
result_list = []
for pal in words:
    if pal == pal[::-1]:
        result_list.append(pal)

print(result_list)
print(f'Found palindrome {result_list.count(palindrome)} times')
