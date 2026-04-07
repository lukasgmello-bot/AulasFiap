"""
elif <condição2>:
     <bloco verdadeiro>
else:
     <bloco outros>

Exemplo:
Fazer um menu com 3 exercicios onde o usuário escolha qual ele vai executar

"""

dia = int(input("Digite o dia: "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda-Feira")
elif dia == 3:
    print("Terça-Feira")
elif dia == 4:
    print("Quarta-Feira")
elif dia == 5:
    print("Quinta-Feira")
elif dia == 6:
    print("Sexta-Feira")
elif dia == 7:
    print("Sábado")
else:
    print("Dia inválido")