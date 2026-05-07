# Verificar palíndromo
# Ex: "arara" → é igual ao contrário

# Pedimos a palavra e padronizamos para minúsculas
entrada = input("Digite uma palavra ou frase: ").lower()

# Removemos espaços (importante para frases como "A cara rajada da jararaca")
palavra = entrada.replace(" ", "")

# Invertemos a palavra usando fatiamento
palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print(f"'{entrada}' é um palíndromo! ✅")
else:
    print(f"'{entrada}' NÃO é um palíndromo. ❌")