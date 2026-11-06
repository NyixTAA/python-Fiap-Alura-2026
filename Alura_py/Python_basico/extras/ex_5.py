inicio = int(input('Digite o inicio da sequência: '))
fim = int(input('Digite o fim da sequênca: '))
total_primos = 0
soma_primos = 0

print(f'\nOs números primos de {inicio} a {fim} são:')
for i in range(inicio, fim + 1):
    if i < 2:
        continue
    
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
        total_primos += 1
        soma_primos += i

print(f'Números primos totais na sequência: {total_primos}\nSoma dos números primos na sequência: {soma_primos}')