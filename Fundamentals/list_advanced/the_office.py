employ_happiness = [int(s) for s in input().split()]
factor = int(input())
multiply_list = [element * factor for element in employ_happiness]
average = sum(multiply_list) / len(employ_happiness)
happy_people = 0
for x in multiply_list:
    if x > average:
        happy_people += 1

if happy_people >= len(employ_happiness) / 2:
    print(f'Score: {happy_people}/{len(employ_happiness)}. Employees are happy!')
else:

    print(f'Score: {happy_people}/{len(employ_happiness)}. Employees are not happy!')

