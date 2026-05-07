# Ordem crescente
# Peça 3 números e mostre em ordem crescente

numeros = []

# Pedindo os 3 números
for i in range(1, 4):
    num = float(input(f"Digite o {i}º número: "))
    numeros.append(num)

# Ordenando a lista de forma crescente
numeros.sort()

print(f"\nNúmeros em ordem crescente: {numeros}")