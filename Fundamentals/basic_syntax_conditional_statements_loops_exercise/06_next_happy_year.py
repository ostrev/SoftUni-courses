year = int(input())

year += 1
while True:
    year_string = str(year)
    len_year = len(year_string)
    set_year = set(year_string)
    len_set = len(set_year)
    if len_year == len_set:
        print(year)
        break
    year += 1
