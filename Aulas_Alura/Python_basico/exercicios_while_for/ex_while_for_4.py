temp = float(input('Digite uma temperatura: '))

soma = 0
calc = 0

while temp != -273:
    soma += temp
    calc += 1
    temp = float(input('Digite outra temperatura: '))

media = soma / calc
print(f'A média das temperaturas é de: {media}')