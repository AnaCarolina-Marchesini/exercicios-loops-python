'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''

# laço para repetição
while True:
    # vai pedir o nome do usuário
    nome_usuario = input('Digite o nome de usuário: ')
    # vai pedir a senha
    senha = input('Digite a senha: ')

    # condição para verificar se o nome é igual a senha
    if nome_usuario == senha:
        # se for igual o print vai ser exibido
        print('O nome de usuário não pode ser igual a senha!')
        # e vai voltar para o começo do programa e perguntar novamente
        continue
    # se a condição for atingida
    else:
        # o print vai se exibido
        print(f'Acesso permitido! Bem-vindo {nome_usuario}!')
        # e o programa encerra
        break