# Menu com loop

# Menu infinito:

# 1 - Olá
# 2 - Sair

# Só sai quando escolher 2

while True:
    print("\n--- MENU INTERATIVO ---")
    print("1 - Olá")
    print("2 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\nOlá! Seja muito bem-vindo(a)!")
    elif opcao == "2":
        print("\nSaindo do programa... Até logo!")
        break  # Este comando encerra o loop while
    else:
        print("\nOpção inválida! Tente novamente.")