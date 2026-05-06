# Número secreto

# Crie um número fixo (ex: 7)
# Usuário tenta adivinhar até acertar

numero_secreto = 7
tentativa = int(input('Tente adivinhar o número secreto inserindo um número: '))

if tentativa == numero_secreto:
    print(f'Parabéns! Você acertou! O número secreto é {numero_secreto}')
else:
    print('Você errou tente novamente...')