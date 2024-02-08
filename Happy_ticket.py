def is_happy_ticket(ticket):
    count_symbol = len(ticket)
    middle = int(count_symbol / 2)
    first_part = ticket[0:middle]
    second_part = ticket[middle:]
    index = 0
    sum_first_part = 0
    while index < middle:
        symbol = int((str(first_part)[index]))
        sum_first_part = sum_first_part + symbol
        index = index + 1
    index = 0
    sum_second_part = 0
    while index < middle:
        symbol = int(str(second_part)[index])
        sum_second_part = int(sum_second_part) + symbol
        index = index + 1
    if (sum_first_part == sum_second_part):
        return('true')
    else:
        return('false')

print(is_happy_ticket('1111001121'))