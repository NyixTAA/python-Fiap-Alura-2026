#1:
'''
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))

print(f'A soma dos valores é igual a: {valor1 + valor2 + valor3}')
'''

#2:
'''
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

print(f'O produto dos valores é igual a: {valor1 * valor2}')
'''

#3:
'''
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

if valor1 == 0 or valor2 == 0:
    print('O valor do denominador não pode ser 0')
else:
    print(f'A divisão dos valores é igual a: {valor1 / valor2}')
'''

#4:
'''
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

print(f'A exponenciação dos valores é igual a: {valor1 ** valor2}')
'''

#5:
'''
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

if valor1 == 0 or valor2 == 0:
    print('O valor do denominador não pode ser 0')
else:
    print(f'A divisão inteira dos valores é igual a: {valor1 // valor2}')
'''

#6:
'''
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

if valor1 == 0 or valor2 == 0:
    print('O valor do denominador não pode ser 0')
else:
    print(f'O resto da divisão dos valores é igual a: {valor1 % valor2}')
'''

#7:
'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

print(f'A média das notas é: {(nota1 + nota2 + nota3) / 3}')
'''

#8:
'''
numero1 = 5
numero2 = 12
numero3 = 20
numero4 = 15

print(f'A média ponderada dos numeros é: {(numero1 * 1 + numero2 * 2 + numero3 * 3 + numero4 * 4) / (1 + 2 + 3 + 4)}')
'''

#9:
'''
frase = input('Digite uma frase: ')

frase = frase.replace('s','$')

print(frase)
'''