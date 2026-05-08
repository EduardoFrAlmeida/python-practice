# Simular carrinho

# Crie lista de produtos
# Mostre todos e o total (preço fictício)

# Criando a lista de produtos (Carrinho)
carrinho = [
    {"produto": "Teclado", "preco": 150.00},
    {"produto": "Mouse", "preco": 85.50},
    {"produto": "Monitor", "preco": 950.00},
    {"produto": "Fone de Ouvido", "preco": 200.00}
]

total = 0

print("--- SEU CARRINHO ---")
for item in carrinho:
    nome = item["produto"]
    preco = item["preco"]
    
    print(f"Produto: {nome:<15} | Preço: R$ {preco:>8.2f}")
    
    # Somando ao total
    total += preco

print("-" * 35)
print(f"TOTAL DA COMPRA: R$ {total:.2f}")