# Contar palavras

# Peça uma frase e conte quantas palavras tem

frase = input("Digite uma frase: ")

# O .split() divide a frase nos espaços e gera uma lista
lista_palavras = frase.split()

# O len() conta quantos itens existem nessa lista
quantidade = len(lista_palavras)

print(f"Essa frase contém {quantidade} palavra(s).")