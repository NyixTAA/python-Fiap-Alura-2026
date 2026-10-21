#1:
'''
numero1 = int(input('Insira o primeiro valor: '))
numero2 = int(input('Insira o segundo valor: '))

if numero1 > numero2:
    print(f'{numero1} é maior que {numero2}')
elif numero1 < numero2:
    print(f'{numero2} é maior que {numero1}')
else:
    print('Os dois valores são iguais')
'''

#2:
'''
porcent_cresc = float(input('Insira o valor do percentual de crescimento de produção da empresa: '))

if porcent_cresc >= 0.1:
    print(f'Houve um crescimento positivo!')
elif porcent_cresc <= 0:
    print(f'Houve um decrescimento.')
'''

#3:
'''
letra = input('Digite uma letra: ')

if letra in 'aeiou':
    print('A letra digitada é uma vogal!')
else:
    print('A letra digitada é uma consoante!')
'''

#4:
'''
preco_ano1 = float(input('Digite o preço médio do carro no primeiro ano: '))
preco_ano2 = float(input('Digite o preço médio do carro no segundo ano: '))
preco_ano3 = float(input('Digite o preço médio do carro no terceiro ano: '))

if preco_ano1 >= preco_ano2 and preco_ano1 >= preco_ano3:
    maior = preco_ano1
elif preco_ano2 >= preco_ano1 and preco_ano2 >= preco_ano3:
    maior = preco_ano2
else:
    maior = preco_ano3

if preco_ano1 <= preco_ano2 and preco_ano1 <= preco_ano3:
    menor = preco_ano1
elif preco_ano2 <= preco_ano1 and preco_ano2 <= preco_ano3:
    menor = preco_ano2
else:
    menor = preco_ano3

print(f'O maior preço registrado deste veículo em 3 anos é de: R${maior:.2f} e o menor preço é de R${menor:.2f}')
'''

#5:
'''
produto1 = float(input('Digite o valor do primeiro produto: '))
produto2 = float(input('Digite o valor do segundo produto: '))
produto3 = float(input('Digite o valor do terceiro produto: '))

if produto1 <= produto2 and produto1 <= produto3:
    menor = f'primeiro produto, que custa: R$ {produto1}'
elif produto2 <= produto1 and produto2 <= produto3:
    menor = f'segundo produto, que custa: R$ {produto2}'
else:
    menor = f'terceiro produto, que custa: R$ {produto3}'

print(f'O produto mais barato é o {menor}')
'''

#6:
'''
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

if numero1 >= numero2 and numero2 >= numero3:
    maior, meio, menor = numero1, numero2, numero3
elif numero1 >= numero3 and numero3 >= numero2:
    maior, meio, menor = numero1, numero3, numero2
elif numero2 >= numero1 and numero1 >= numero3:
    maior, meio, menor = numero2, numero1, numero3
elif numero2 >= numero3 and numero3 >= numero1:
    maior, meio, menor = numero2, numero3, numero1
elif numero3 >= numero1 and numero1 >= numero2:
    maior, meio, menor = numero3, numero1, numero2
elif numero3 >= numero2 and numero2 >= numero1:
    maior, meio, menor = numero3, numero2, numero1

print(f'Os números ordenados em ordem decrescente são: {maior},{meio},{menor}')
'''

#7:
'''
turno = input('Digite em qual turno você estuda (manhã, tarde ou noite): ')
if turno == 'manhã' or turno == 'manha':
    print('Bom dia!')
elif turno == 'tarde':
    print('Boa tarde!')
elif turno == 'noite':
    print('Boa noite!')
else:
    print('Digite um turno válido!')
'''

#8:
'''
numero = int(input('Digite um número inteiro: '))
if numero % 2 == 0:
    print('O valor é par!')
else:
    print('O valor é impar!')
'''

#9:
'''
numero = float(input('Digite um número: '))
if numero % 1 == 0:
    print('O número digitado é um número inteiro!')
else:
    print('O número digitado é um valor decimal!')
'''