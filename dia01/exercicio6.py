#python-print

# A ideia é imprimir os números um ao lado do outro, sem espaços e sem pular linha.

n = int(input('Digite um Número: '))

    # Começamos de 1 e vamos até n (por isso n + 1)
for i in range(1, n + 1):
    print(i, end="")