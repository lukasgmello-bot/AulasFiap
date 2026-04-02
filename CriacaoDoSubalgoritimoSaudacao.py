# DEFINIÇÃO DO PROCEDIMENTO
#def saudacao2(usuario, turno):
#    print(f"{usuario}, {turno}! Bem-vindo à Fiap!")


# chamada do procedimento no programa principal
#saudacao2("Lucas Mello", "Boa noite")

# DEFINIÇÃO DO PROCEDIMENTO
def saudacao2(usuario, hora):
    if hora < 12:
        turno = "Bom dia"
    elif hora < 18:
        turno = "Boa tarde"
    else:
        turno = "Boa noite"
    print(f"{usuario}, {turno}! Seja bem-vindo à FIAP!")


# CHAMADA DO PROCEDIMENTO NO PROGRAMA PRINCIPAL
saudacao2("Lucas Mello", 22)
