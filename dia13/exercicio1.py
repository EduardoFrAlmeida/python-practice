# Multiplicação manual

# Sem usar *, multiplique dois números usando loop

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

resultado = 0

# Somamos o num1 à variável resultado, num2 vezes
for _ in range(abs(num2)):
    resultado += num1

# Ajuste para caso o segundo número seja negativo
if num2 < 0:
    resultado = -resultado

print(f"O resultado da multiplicação é: {resultado}")