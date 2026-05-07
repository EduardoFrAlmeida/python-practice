# Contar letras específicas
# Peça uma palavra e conte quantas vezes aparece a letra "a"


palavra = input("Digite uma palavra: ").lower()

# Contando quantas vezes a letra "a" aparece
quantidade = palavra.count("a")

print(f"A letra 'a' aparece {quantidade} vez(es) na palavra.")