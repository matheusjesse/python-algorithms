def is_anagram(first_string, second_string):
    one = first_string.lower()
    two = second_string.lower()
    first = ''.join(alphabetical_order(list(one.strip())))
    second = ''.join(alphabetical_order(list(two.strip())))

    return (first, second, first == second)


def alphabetical_order(string_list):
    if not string_list:
        return []
    return (alphabetical_order(
            [x for x in string_list[1:] if x < string_list[0]])
            + [string_list[0]] +
            alphabetical_order(
            [x for x in string_list[1:] if x >= string_list[0]]))
