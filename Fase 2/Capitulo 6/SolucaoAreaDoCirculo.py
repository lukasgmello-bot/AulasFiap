# DEFINIÇÃO DA FUNÇÃO
def valor_de_pi():
    return 3.14159

# CHAMADA DA FUNÇÃO NO PROGRAMA PRINCIPAL DENTRO DE UM CÁLCULO
raio = float(input("Digite o raio: "))
area_circulo = valor_de_pi() * raio ** 2
print(f"Área do circulo com raio {raio} é {area_circulo}")