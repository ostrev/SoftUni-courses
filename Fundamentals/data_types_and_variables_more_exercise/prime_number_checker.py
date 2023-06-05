is_number_prime = int(input())
result = True
for number in range(2, is_number_prime):
    if is_number_prime % number == 0:
        result = False
        break
print(result)
