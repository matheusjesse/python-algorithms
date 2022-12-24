def is_palindrome_iterative(word):
    if word == "":
        return False
# inversão palavras
# https://pt.stackoverflow.com/questions/401489/inverter-as-palavras-de
# -uma-frase-mantendo-a-ordem-delas-na-frase
    return word == word[::-1] 
