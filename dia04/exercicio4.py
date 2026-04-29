# Menu simples
# Mostre:
# 1 - Ver saldo
# 2 - Sair
# E responda de acordo com a escolha

# Exibição do Menu
print("--- MENU BANCÁRIO ---")
print("1 - Ver saldo")
print("2 - Sair")
print("---------------------")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    saldo = 1500.50
    print(f"Seu saldo atual é: R$ {saldo}")
elif opcao == "2":
    print("Saindo do sistema... Até logo!")
else:
    print("Opção inválida! Por favor, escolha 1 ou 2.")  