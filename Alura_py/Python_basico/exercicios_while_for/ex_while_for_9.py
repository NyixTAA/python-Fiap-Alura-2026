candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
candidato_4 = 0
nulo = 0
branco = 0
i = 0

while i < 20:
    voto = input('\nDigite seu voto: (1,2,3,4): ')
    if voto in ('1','2','3','4','5','6'):
        if voto == '1':
            candidato_1 += 1
        elif voto == '2':
            candidato_2 += 1
        elif voto == '3':
            candidato_3 += 1
        elif voto == '4':
            candidato_4 += 1
        elif voto == '5':
            nulo += 1
        else:
            branco += 1
        i += 1    
    else:
        print('\nNúmero de candidato inválido!')
        continue

print(f'\nVotos no candidato Nº 1: {candidato_1}')
print(f'Votos no candidato Nº 2: {candidato_2}')
print(f'Votos no candidato Nº 3: {candidato_3}')
print(f'Votos no candidato Nº 4: {candidato_4}')
print(f'Votos em branco: {branco}; Votos brancos em relação ao total de votos: {branco / 20 * 100}%')
print(f'Votos em nulos: {nulo}; Votos nulos em relação ao total de votos: {nulo / 20 * 100}%')