def is_palindrome_iterative(word):
    if word == "":
        return False

    reverted_string = reverse_string(word)

    if word == reverted_string:
        return True
    else:
        return False


def reverse_string(string):
    revert_string = ''
    string_index = len(string) - 1
    while string_index >= 0:
        revert_string = revert_string + string[string_index]
        string_index = string_index - 1
    return revert_string
