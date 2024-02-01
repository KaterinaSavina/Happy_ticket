def is_happy_ticket(ticket):
    str_ticket = str(ticket)
    count_symbol = int(len(str_ticket))
    middle = int(count_symbol / 2)
    first_part = str_ticket[0:middle]
    second_part = str_ticket[middle:]
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
        #print('true')
        return('true')
    else:
        #print('false')
        return('false')

print(is_happy_ticket(101))