def is_anagram(first_string, second_string):
    first = alphabetical_order(first_string)
    second = alphabetical_order(second_string)
    check_string = first == second

    return (first, second, check_string)


def alphabetical_order(string):
    lowered_string = string.lower()
    unsorted = list(lowered_string.strip())
    sort_string = ""

    while unsorted:
        smallest = min(unsorted)
        sort_string += smallest
        unsorted.pop(unsorted.index(smallest))

    return sort_string
