winning_symbols = ['@', '#', '$', '^']


def is_jackpot(ticket_j):
    for i in winning_symbols:
        if i * 20 in ticket_j:
            print(f'ticket "{ticket_j}" - {10}{i} Jackpot!')
            return True
    return False


def is_winning(ticket_win):
    ticket_left = ticket_win[0:10]
    ticket_right = ticket_win[10:]
    for i in winning_symbols:
        if i * 9 in ticket_left and i * 9 in ticket_right:
            print(f'ticket "{ticket}" - {9}{i}')
            return True
        elif i * 8 in ticket_left and i * 8 in ticket_right:
            print(f'ticket "{ticket}" - {8}{i}')
            return True
        elif i * 7 in ticket_left and i * 7 in ticket_right:
            print(f'ticket "{ticket}" - {7}{i}')
            return True
        elif i * 6 in ticket_left and i * 6 in ticket_right:
            print(f'ticket "{ticket}" - {6}{i}')
            return True

    return


command = input().split(', ')
for ticket in command:
    ticket = ticket.strip()
    if len(ticket) == 20: # проверка дали е валиден
        if is_jackpot(ticket):
            continue
        elif is_winning(ticket):
            continue
        else:
            print(f"ticket \"{ticket}\" - no match")
    else:
        print("invalid ticket")

