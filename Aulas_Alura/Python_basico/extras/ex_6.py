altura = int(input('Digite a altura desejada das pirâmides (3 - 10): '))

if altura < 3 or altura > 10:
    print('Digite uma altura válida (3 - 10)!')
else:
    print('Figura A:')
    for i in range(altura + 1):
        for j in range(i):
            print(i, end=' ')
        print()

    print('\nFigura B:')
    for i in range(altura, 0, -1):
        for j in range(i):
            print(i, end=' ')
        print()