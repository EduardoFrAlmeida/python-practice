# List Comprehensions

# A Solução com List Comprehension
# A List Comprehension permite condensar toda essa estrutura em uma única linha. A sintaxe básica é:
# [expressão for item in iterável if condição]

x = int(input('Digite o valor de X: '))
y = int(input('Digite o valor de Y: '))
z = int(input('Digite o valor de Z: '))
n = int(input('Digite o valor de N: '))
    
print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n])


