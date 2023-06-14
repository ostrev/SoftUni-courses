command = input()
dic_company = {}
while command != 'End':
    company_name, user = command.split(' -> ')
    if company_name not in dic_company:
        dic_company[company_name] = []
    if user not in dic_company[company_name]:
        dic_company[company_name].append(user)

    command = input()
sort_dic = sorted(dic_company.items(), key=lambda kvp: kvp[0])
for com_name, users in sort_dic:
    print(f'{com_name}')
    for i in users:
        print(f'-- {i}')
