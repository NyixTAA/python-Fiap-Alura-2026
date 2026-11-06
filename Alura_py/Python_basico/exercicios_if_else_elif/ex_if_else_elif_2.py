print('Os seguintes números solicitados representarão os lados de um triângulo.')
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
numero3 = float(input('Digite o terceiro número: '))

if numero1 + numero2 > numero3 and numero3 + numero2 > numero1 and numero3 + numero1 > numero2:
    if numero1 == numero2 == numero3:
        tipo_triangulo = 'Equilátero'
    elif numero1 == numero2 or numero2 == numero3 or numero1 == numero3:
        tipo_triangulo = 'Isósceles'
    else:
        tipo_triangulo = 'Escaleno'
    print(f'Os lados digitados igualam à um triângulo {tipo_triangulo}!')
else:
    print('Os números atrelados aos lados digitados não podem formar um triângulo.')