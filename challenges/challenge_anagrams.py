def is_anagram(first_string, second_string):
    one = first_string.lower()
    two = second_string.lower()
    first = ''.join(alphabetical_order(list(one.strip())))
    second = ''.join(alphabetical_order(list(two.strip())))

    if one == "" or two == "":
        return (first, second, False)

    return (first, second, first == second)


def alphabetical_order(string_list):
    if not string_list:
        return []
    return (alphabetical_order(
            [char for char in string_list[1:] if char < string_list[0]])
            + [string_list[0]] +
            alphabetical_order(
            [char for char in string_list[1:] if char >= string_list[0]]))
