senha = int(input('Digite uma senha de quatro dígitos: '))

while senha < 1000 or senha > 9999:
    if senha == 0:
        print('A senha não pode ser 0.')
        senha = int(input('Digite uma senha de quatro dígitos: '))
    else:
        print('Senha inválida, a senha deve conter 4 digitos.')
        senha = int(input('Digite uma senha de quatro dígitos: '))

print('\n---- MODO DE AUTENTICAÇÃO ----\n')
tentativas = 3

while True:
    print(f'Digite a senha novamente.\nTentativas: {tentativas}\n')
    autenticacao = int(input('Senha: '))
    if autenticacao == senha:
        print('Acesso concedido!')
        break
    else:
        print('Senha incorreta!\n')
        tentativas -= 1
    if tentativas == 0:
        print('Acesso negado.')
        break