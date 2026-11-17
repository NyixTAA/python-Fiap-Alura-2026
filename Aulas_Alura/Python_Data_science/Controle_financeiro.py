import os
import time
import subprocess

def limpar_terminal():
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run(['clear'])

print('---- Bem vindo ao Controle Financeiro! ----\n')
nome = input('Digite o seu nome: ')
while nome.isalpha() == False:
    limpar_terminal()
    print('Seu nome não deve conter números, espaços ou carácteres especiais.\n')
    nome = input('Digite o seu nome: ')
        
saldo = 0
opcao = 0
lista_gastos = []
soma_gastos = 0

def menu():
    print(f'Saldo Atual: R$ {saldo - soma_gastos:.2f}\n')
    print('1 - Adicionar saldo\n2 - Adicionar gastos\n3 - Verificar gastos\n4 - Verificar resumo do mês\n5 - Encerrar programa\n')

def adicionar_saldo(saldo):
    limpar_terminal()
    adicionar = input('Digite quanto gostaria de adicionar à conta (0 para retornar): ')
    while type(adicionar) != float or adicionar <= 0:
        try:
            adicionar = float(adicionar)
            if adicionar < 0:
                limpar_terminal()
                print('O valor digitado deve ser positivo, se gostaria de retornar, digite 0.')
                adicionar = input('Digite quanto gostaria de adicionar à conta (0 para retornar): ')
                continue
            if adicionar == 0:
                break
            if adicionar > 10000:
                limpar_terminal()
                print('Só é possível adicionar R$ 10.000 por vez.')
                adicionar = input('Digite quanto gostaria de adicionar à conta (0 para retornar): ')
        except ValueError:
            limpar_terminal()
            print('Digite um valor válido!')
            print('--------------------------------------------------------------\n')
            adicionar = input('Digite quanto gostaria de adicionar à conta: ')
    limpar_terminal()
    saldo += adicionar
    if adicionar > 0:
        print(f'\nR$ {adicionar:.2f} Adicionado à conta!')
        time.sleep(1.5)
    return saldo

def adicionar_gastos(soma_gastos, saldo):
    limpar_terminal()
    print('---- Sessão de gastos ----\n')
    continuar = 1
    while continuar != 0:
        gasto = input('Digite o nome do gasto: ')
        while gasto == '':
            limpar_terminal()
            print('O nome do gasto não pode ser vazio!\n')
            gasto = input('Digite o nome do gasto: ')
        
        valor = input('Digite o preço do gasto: ')
        while type(valor) != float:
            try:
                valor = float(valor)
            except ValueError:
                limpar_terminal()
                print('Digite um valor válido!')
                print('--------------------------------------------------------------\n')
                valor = input('Digite o preço do gasto: ')
        if valor < 0:
            limpar_terminal()
            print('\nHmm, parece que o valor digitado não se enquadra como gasto.')
            print('--------------------------------------------------------------\n')
            print('Caso queira adicionar saldo, digite 2.')
            print('Caso tenha digitado o sinal de menos por acidente, digite 1.')
            print('Caso não tenha sido um acidente, digite 0 para voltar ao menu.\n')
            
            escolha = input('Escolha: ')
            while escolha not in ('1', '0', '2'):
                limpar_terminal()
                print('\nDigite uma opção válida!')
                print('--------------------------------------------------------------\n')
                print('Caso queira adicionar saldo, digite 2.')
                print('Caso tenha digitado o sinal de menos por acidente, digite 1.')
                print('Caso não tenha sido um acidente, digite 0 para voltar ao menu.\n')
                escolha = input('Escolha: ')
                
            if escolha == '1':
                limpar_terminal()
                valor = valor * -1
                soma_gastos += valor
                lista_gastos.append({gasto.capitalize(): f'R$ {valor:.2f}'})
                print(f'Gasto {gasto.capitalize()} (R$ {valor:.2f}) adicionado com sucesso!')
            elif escolha == '2':
                limpar_terminal()
                saldo = adicionar_saldo(saldo)
                break
            else:
                limpar_terminal()
                break
        elif valor == 0:
            limpar_terminal()
            print('Se custa 0 reais não é um gasto!')
        else:
            limpar_terminal()
            print(f'Gasto {gasto.capitalize()} (R$ {valor:.2f}) adicionado com sucesso!')
            soma_gastos += valor
            lista_gastos.append({gasto.capitalize(): (f'R$ {valor:.2f}')})
        escolha = input('\n1 - Adicionar novo valor\n0 - Encerrar\n')
        limpar_terminal()
        while escolha not in ('1','0'):
            limpar_terminal()
            print('\nDigite uma opção válida!')
            print('--------------------------------------------------------------\n')
            escolha = input('\n1 - Adicionar novo valor\n0 - Encerrar\n')
        if escolha == '0':
            break
    return soma_gastos, saldo

def verificar_gastos():
    limpar_terminal()
    print('---- Gastos do mês ----\n')
    if lista_gastos == []:
        print('Nenhum gasto foi registrado nesse mês ainda, uhul!')
    for i, j in enumerate(lista_gastos, start=1):
        for chave, valor in j.items():
            print(f'{i} - {chave}: {valor}')
    input('\nPressione qualquer tecla para retornar.')

def resumo_do_mes():
    limpar_terminal()
    print('---- Resumo do mês ----\n')
    print(f'Saldo total: R$ {saldo:.2f}')
    print(f'Gastos totais: R$ {soma_gastos:.2f}')
    if (saldo - soma_gastos) >= 0:
        print(f'Saldo restante: R$ {saldo - soma_gastos:.2f}')
    else:
        print(f'Você deve R$ {(saldo - soma_gastos) * -1:.2f}')
    opcao = input('Pressione qualquer tecla para retornar.')

try:
    while opcao != 5:
        limpar_terminal()
        print(f'\nOlá {nome.capitalize()}, o que faremos hoje?\n')
        menu() 
        opcao = input('Digite a opção desejada: ')
        while opcao not in ('1','2','3','4','5'):
            limpar_terminal()
            print(f'\nOlá {nome}, o que faremos hoje?\n')
            menu()
            print('Digite uma opção válida!\n')
            opcao = input('Digite a opção desejada: ')
        opcao = int(opcao)
        
        if opcao == 1:
            saldo = adicionar_saldo(saldo)
            
        elif opcao == 2:
            soma_gastos, saldo = adicionar_gastos(soma_gastos, saldo)
                    
        elif opcao == 3:
            verificar_gastos()
        elif opcao == 4:
            resumo_do_mes()
except Exception as e:
    print(type(e),f'Erro {e}')
    
finally:
    print('Programa finalizado, até a próxima!')