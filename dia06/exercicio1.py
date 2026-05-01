# Simular login
# Crie:
# usuário = "admin"
# senha = "1234"
# Peça login e valide


usuario_cadastrado = 'admin'
senha_cadastrada = '1234'

user_login = input('Digite seu usuário cadastrado: ')
user_password = input('Digite sua Senha: ')

if user_login == usuario_cadastrado and user_password == senha_cadastrada:
    print('Login realizado com sucesso, Bem vindo adimin!')
else:
    print('Erro: Usuário ou senha incorretos, tente novamente.')