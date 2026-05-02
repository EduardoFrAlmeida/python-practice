# Sistema simples

# Menu:
# cadastrar nome
# listar nomes

nomes = []

while True:
    print("\n--- SISTEMA DE NOMES ---")
    print("1 - Cadastrar nome")
    print("2 - Listar nomes")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        novo_nome = input("Digite o nome para cadastrar: ")
        nomes.append(novo_nome) # Adiciona o nome ao final da lista
        print(f"✅ {novo_nome} cadastrado com sucesso!")

    elif opcao == "2":
        if len(nomes) == 0: # Verifica se a lista está vazia
            print("⚠️ A lista está vazia.")
        else:
            print("\n--- LISTA DE NOMES ---")
            for i, nome in enumerate(nomes, 1): # Lista com numeração
                print(f"{i}. {nome}")

    elif opcao == "3":
        print("Saindo do sistema...")
        break # Encerra o loop while

    else:
        print("❌ Opção inválida!")