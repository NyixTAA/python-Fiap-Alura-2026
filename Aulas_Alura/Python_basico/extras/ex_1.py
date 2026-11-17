numero = int(input('Digite um número inteiro: '))
total_dig = 0
total_par = 0
total_impar = 0
soma_dig = 0

while numero > 0:
    if numero % 10 == 0:
        total_dig += 1
        if numero % 2 == 0:
            total_par += 1
        else:
            total_impar += 1
        numero /= 10
    else:
        if numero % 2 == 0:
            total_par += 1
        else: total_impar += 1
        soma_dig += numero % 10
        numero //= 10
        total_dig += 1

print(f'\nTotal de dígitos: {total_dig}')
print(f'Dígitos pares: {total_par}')
print(f'Dígitos ímpares: {total_impar}')
print(f'Soma dos dígitos: {int(soma_dig)}')