def is_palindrome_iterative(word):
    if not word:
        return False
# inversão palavra
# https://pt.stackoverflow.com/questions/401489/inverter-as-palavras-de
# -uma-frase-mantendo-a-ordem-delas-na-frase
    return word[::-1] == word
