number_of_electrons = int(input())
shell_count = 1
list_shell = []
while number_of_electrons > 0:
    electrons = 2 * shell_count**2
    if number_of_electrons >= electrons:
        number_of_electrons -= electrons
        list_shell.append(electrons)
        shell_count +=1
    else:
        list_shell.append(number_of_electrons)
        break
print(list_shell)
