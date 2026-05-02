# Lista de usuários
# Crie lista com nomes

# Verifique se um nome existe

usuarios = ['alice', 'bruno', 'caio', 'deborah']

busca = input('Digite o nome que deseja verificar: ').lower()

if busca in usuarios:
    print(f'O usuário {busca} foi encontrado na lista!')
else:
    print(f'O usuário {busca} não existe na lista')    