command = input()
total_sum = 0
discount = 0
total_price_discount = 0
while command != 'special' and command != 'regular':

    if float(command) <= 0:
        print("Invalid price!")
    else:
        total_sum += float(command)
    command = input()

if total_sum == 0:
    print("Invalid order!")
else:
    taxes = total_sum * 0.2
    if command == 'special':
        total_price_discount = total_sum + taxes
        total_price_discount = total_price_discount * 0.9

    elif command == 'regular':
        total_price_discount = total_sum + taxes
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_sum:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          f"-----------\n"
          f"Total price: {total_price_discount:.2f}$")
