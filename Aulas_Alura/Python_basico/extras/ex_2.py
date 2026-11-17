qnt = int(input('Informe quantos números você gostaria de digitar: '))
media_numeros = 0

for i in range(qnt):
    n = int(input(f'Digite o {i + 1}º número: '))
    media_numeros += n
    
    if i == 0:
        maior_numero = n
        segundo_maior = n
        menor_numero = n
    else:
        if n < menor_numero:
            menor_numero = n
            
        if n > maior_numero:
            segundo_maior = maior_numero
            maior_numero = n
        elif n > segundo_maior or i == 1:
            segundo_maior = n

print('\n--- RESULTADO ---')
print(f'Maior número: {maior_numero}')
print(f'Segundo maior número: {segundo_maior}')
print(f'Menor número: {menor_numero}')
print(f'Média dos números: {media_numeros / qnt:.2f}')