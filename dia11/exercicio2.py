# Somar até parar

# Peça números e vá somando
# Quando digitar 0 → para e mostra total

soma = 0

while True:
    numero = float(input('Digite um número (Ou zero 0 para parar: )'))

    if numero == 0:
        break

    soma += numero

print(f"\n--- FIM ---")
print(f"A soma total de todos os números digitados é: {soma}")