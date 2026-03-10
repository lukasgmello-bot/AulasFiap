somatoria = 0
print("Digite números ou 0 para finalizar...")
while True:
          num = float(input())
          somatoria = somatoria + num
          if num == 0:
            break
print(f"Somatoria = {somatoria}")