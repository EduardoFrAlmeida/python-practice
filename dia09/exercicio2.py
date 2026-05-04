# Verificar número positivo
# Peça um número:
# positivo
# negativo
# zero

numero = float(input('Digite um número: '))

if numero > 0:
    print('O número é positivo.')
elif numero < 0:
    print('O número é negativo.')   
else:
    print('O número é zero.')