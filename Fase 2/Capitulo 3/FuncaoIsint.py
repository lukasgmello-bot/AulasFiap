# Função isinit()
def isint(s: str) -> bool:
    digito = "0123456789"
    valido = True
    if s[0] == "-" or s [0] == "+" or s[0] in digito:
        for i in range(1, len(s)):
            if s[i] not in digito:
                valido = False
    else:
        valido = False
    return valido

# Teste da função isint()
print(isint("j33i"))  #False
print(isint("99"))   #True
print(isint("4@34"))  #False
print(isint("-45")) #True
print(isint("+44")) #True