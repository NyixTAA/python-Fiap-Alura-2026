idade = int(input('Informe a idade (ou um número negativo para encerrar): '))

contador_0_25 = 0
contador_26_50 = 0
contador_51_75 = 0
contador_76_100 = 0

while idade >= 0:
    if idade < 26:
        contador_0_25 += 1
    elif idade < 51:
        contador_26_50 += 1
    elif idade < 76:
        contador_51_75 += 1
    else:
        contador_76_100 += 1
    idade = int(input('Informe a idade (ou um número negativo para encerrar): '))

print(f'Pessoas de 0 - 25 anos: {contador_0_25}')
print(f'Pessoas de 26 - 50 anos: {contador_26_50}')
print(f'Pessoas de 51 - 75 anos: {contador_51_75}')
print(f'Pessoas de 76 - 100 anos: {contador_76_100}')