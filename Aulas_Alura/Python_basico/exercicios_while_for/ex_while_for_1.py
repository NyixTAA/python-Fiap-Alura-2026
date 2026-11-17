numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
i = numero1 + 1

if numero1 == numero2:
    print('Digite números diferentes!')
elif numero1 == numero2 - 1:
    print('Não há intervalo entre esses números!')
else:
    while i < numero2:
        print(i)
        i += 1