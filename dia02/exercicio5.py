# Par ou ímpar
# Peça um número e diga se é par ou ímpar

# Pedimos o número e convertemos para inteiro (int)
numero = int(input('Digite um número inteiro: '))


# Verificamos o resto da divisão por 2

if numero % 2 == 0:
    print('O número {numero} é PAR!')
else:
    print('O número {numero} é ÍMPAR!')