# Média
# Peça 3 notas e calcule a média

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))
media = (nota1 + nota2 + nota3 / 3)

if media >= 7:
    print(f'Aprovado! Sua média foi de {media} ')
else:
    print(f'Reprovado! Sua média foi de {media}')    
