import re
number = int(input())
count = 0
for _ in range(number):
    text = input()
    patter = r'U\$([A-Z][a-z]{2,})U\$P@\$([A-Za-z]{5,}[0-9]+)P@\$'

    matches = re.search(patter, text)
    if matches:
        count += 1
        print(f"Registration was successful")
        print(f"Username: {matches.group(1)}, Password: {matches.group(2)}")
    else:
        print("Invalid username or password")
print(f'Successful registrations: {count}')