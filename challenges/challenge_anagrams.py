def is_anagram(first_string, second_string):
    first = alphabetical_order(first_string)
    second = alphabetical_order(second_string)

    return (first, second, first == second)


def alphabetical_order(string):
    lowered_string = teste.lower()
    sort_string = ""

    while lowered_string:
        smallest = min(lowered_string)
        sort_string += smallest
        lowered_string = lowered_string.replace(smallest, '', 1)

    return sort_string
