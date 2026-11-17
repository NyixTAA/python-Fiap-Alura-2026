numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

operacao = input(f'Digite a operação matemática que gostaria de realizar com os números {numero1} e {numero2} (+,-,*,/):')
executado = True

if operacao in ('+','-','*','/'):
    if operacao == '+':
        resultado = numero1 + numero2
        nome_operacao = 'soma'
    elif operacao == '-':
        resultado = numero1 - numero2
        nome_operacao = 'subtração'
    elif operacao == '*':
        resultado = numero1 * numero2
        nome_operacao = 'multiplicação'
    elif operacao == '/':
        if numero2 != 0:
            resultado = numero1 / numero2
            nome_operacao = 'divisão'
        else:
            print('Não é possível dividir um número por zero!')
            executado = False
    else:
        print('Digite uma operação válida!')
        executado = False

    if executado:
        if resultado > 0:
            class3 = 'Positivo'
        elif resultado < 0:
            class3 = 'Negativo'
        else:
            class3 = 'Neutro (zero)'

        if resultado % 1 == 0:
            resultado = int(resultado)
            class1 = 'Inteiro'
            if resultado % 2 == 0:
                class2 = 'Par'
            else:
                class2 = 'Impar'
        else:
            class1 = 'Decimal'
            resultado = f'{resultado:.2f}'
            class2 = 'Sem paridade (Decimal)'

        print(f'A {nome_operacao} dos números é igual a: {resultado}, é um número {class1}, {class2} e {class3}!')
    
else:
    print('Digite uma operação válida!')