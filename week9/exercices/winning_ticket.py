def is_valid(ticket_nb):
    if len(ticket_nb) == 20:
        return True
    return False


def good_half(half_ticket):
    suite = 0
    last_special_char = []
    for char in half_ticket:
        if char in ('@', '#', '$', '^') and not last_special_char or char in last_special_char:
            last_special_char.append(char)
            suite += 1
            if suite == 6:
                return last_special_char
        else:
            suite = 0
    return False


def jackpot(ticket_nb):
    jackpots = ['$' * 10, '@' * 10]
    first_half = ticket_nb[0:10]
    second_half = ticket_nb[10: 21]
    if first_half in jackpots and second_half in jackpots:
        return f'10{first_half[0]}'
    return False


def winning_ticket(ticket_nb):
    first_half = ticket_nb[0:11]
    second_half = ticket_nb[10: 21]
    result_first_half = good_half(first_half)
    result_second_half = good_half(second_half)
    if jackpot(ticket_nb):
        return f'ticket "{ticket_nb}" - {jackpot(ticket_nb)} Jackpot!'
    elif result_first_half and result_second_half:
        return f'ticket "{ticket_nb}" - {len(result_first_half)}{result_first_half[0]}'
    return f'ticket "{ticket_nb}" - no match'


tickets = [ticket.strip() for ticket in input().split(',')]

for ticket in tickets:
    if is_valid(ticket):
        print(winning_ticket(ticket))
    else:
        print('invalid ticket')
