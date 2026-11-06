for i in range(1,16):
    nota = float(input(f'Digite a nota de 0 a 5 para o {i}º dado: '))
    while nota > 5 or nota < 0:
        nota = float(input(f'Nota inválida, digite uma nota de 0 a 5 para o {i}º dado: '))
print('Notas validadas!')