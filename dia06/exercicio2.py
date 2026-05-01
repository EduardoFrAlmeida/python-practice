# Tentativas de login
# Usuário só pode errar 3 vezes


usuario_cadastrado = 'admin'
senha_cadastrada = '1234'
tentativas = 3

while tentativas > 0:
    print(f'Você tem {tentativas} tentativa(s) restante(s)')

    login = input('Usuário: ')
    senha = input('Senha: ')

    if login == usuario_cadastrado and senha == senha_cadastrada:
        print("✅ Login realizado com sucesso! Bem-vindo.")
        break  # O break encerra o laço while imediatamente se ele acertar
    else:
        tentativas -= 1  # Diminui uma tentativa
        if tentativas > 0:
            print("❌ Usuário ou senha incorretos. Tente novamente.")
        else:
            print("🚫 Acesso bloqueado! Você excedeu o limite de tentativas.")