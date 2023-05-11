from collections import deque as dq

vowels = dq(input().split(' '))
consonants = input().split(" ")

one = list("rose")
two = list("tulip")
three = list("lotus")
four = set(list("daffodil"))

not_found = True
while vowels and consonants:
    vow = vowels.popleft()
    con = consonants.pop()
    if vow in one:
        one.remove(vow)
    if con in one:
        one.remove(con)

    if vow in two:
        two.remove(vow)
    if con in two:
        two.remove(con)

    if vow in three:
        three.remove(vow)
    if con in three:
        three.remove(con)

    if vow in four:
        four.remove(vow)
    if con in four:
        four.remove(con)

    if not one:
        not_found = False
        print(f"Word found: rose")
        break
    if not two:
        not_found = False
        print(f"Word found: tulip")
        break
    if not three:
        not_found = False
        print(f"Word found: lotus")
        break
    if not four:
        not_found = False
        print(f"Word found: daffodil")
        break

if not_found:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")