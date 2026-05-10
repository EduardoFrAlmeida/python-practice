# Validar email simples

# Peça email e verifique se tem "@" e "."

email = input("Digite seu e-mail para cadastro: ").lower()

# Verificando se os caracteres obrigatórios existem
tem_arroba = "@" in email
tem_ponto = "." in email

if tem_arroba and tem_ponto:
    print("E-mail parece válido! ✅")
else:
    # Mostrando o erro específico para ajudar o usuário
    if not tem_arroba:
        print("Erro: O e-mail precisa conter um '@'.")
    if not tem_ponto:
        print("Erro: O e-mail precisa conter um ponto (.).")