# Verificar senha
# Crie uma senha fixa no código e peça pro usuário digitar
# Se errar → "Senha incorreta"

senha_correta = 'python123'

tentativa = input('Digite a senha: ')

if tentativa == senha_correta:
    print('Acesso concedido! Seja bem vindo!')
else:
    print('Senha incorreta! Tente novamente...')    

