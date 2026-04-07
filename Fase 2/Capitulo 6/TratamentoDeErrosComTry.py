try:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    divisao = n1 / n2
    print(f"A divisão de {n1} por {n2} é: {divisao}")
except ValueError:
    print("Erro: Você deve digitar um número válido.")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except:
    print("Ocorreu um erro inesperado. Entre em contato com o administador do sistema.")
else:
    print("A operação foi realizada com sucesso.")
finally:
    print("Obrigado por utilizar o nosso programa.")