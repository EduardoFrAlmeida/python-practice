# Tabuada
# Peça um número e mostre a tabuada dele (1 a 10)

numero = int(input('Digite um número é veja sua tabuada: '))

for i in range(1, 11):
    resultado = numero * i
    print(f' {numero} x {i} = {resultado} ')