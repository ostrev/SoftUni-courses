def password_val(password):
    counter = 0
    counter_two_digit = 0
    if 6 <= len(password) <= 10:
        counter += 1
    else:
        print('Password must be between 6 and 10 characters')
    if password.isalnum():
        counter += 1
    else:
        print('Password must consist only of letters and digits')
    for element in password:
        if element.isdigit():
            counter_two_digit += 1
    if counter_two_digit >= 2:
        counter += 1
    else:
        print('Password must have at least 2 digits')
    if counter >= 3:
        print('Password is valid')


password_check = input()
password_val(password_check)