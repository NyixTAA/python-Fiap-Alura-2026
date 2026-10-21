numero = int(input('Digite um número inteiro: '))

fatorial = 1
i = numero

while i > 0:
    fatorial *= i
    i-=1

print(f'O fatorial de {numero} é {fatorial}')