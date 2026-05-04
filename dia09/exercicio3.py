# Contar caracteres sem espaço
# Peça uma frase e conte quantos caracteres tem (sem contar espaço)

frase = input('Digite uma frase: ')
contador = 0
for char in frase:
    if char != ' ':
        contador += 1
print(f'A frase tem {contador} caracteres (sem contar espaços).')           