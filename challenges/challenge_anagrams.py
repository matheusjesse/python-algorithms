def is_anagram(first_string, second_string):
    first = alphabetical_order(list(first_string.strip()))
    second = alphabetical_order(list(second_string.strip()))

    return (first, second, first == second)


def alphabetical_order(string_list):
    if not string_list:
        return []
    return (alphabetical_order(
            [x for x in string_list[1:] if x < string_list[0]])
            + [string_list[0]] +
            alphabetical_order(
            [x for x in string_list[1:] if x >= string_list[0]]))
