n = int(input())
balance = ''
first_bracket = ''
second_bracket = ''
last_bracket = ''
for i in range(1, n+1):
    random_str = input()
    if last_bracket == random_str:
        balance = False
        break
    if random_str == '(':
        first_bracket = True
        balance = False
    if random_str == ')':
        second_bracket = True
        balance = False
    if first_bracket and second_bracket:
        first_bracket = ''
        second_bracket = ''
        balance = True
    last_bracket = random_str
if balance:
    print('BALANCED')
else:
    print('UNBALANCED')
