# Contar números maiores que 10

# Dada lista [3, 15, 8, 22, 1], conte quantos são > 10

numeros = [3, 5, 80, 22, 75]
contador = 0

for n in numeros:
    if n > 10:
        contador +=1

print(f'Existem {contador} números maiores que 10 na lista!')