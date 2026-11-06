gabarito = ['D','A','C','B','A','D','C','C','A','B']
nota = 0

for i in range(len(gabarito)):
        resposta = input(f'Questão {i + 1}\nDigite sua resposta (A,B,C ou D): ').upper()
        while resposta not in ['A','B','C','D']:
                resposta = input(f'Resposta inválida, a resposta deve ser apenas A,B,C ou D\nDigite sua resposta novamente:').upper()
        if resposta == gabarito[i]:
                nota += 1
print(f'\nSua nota foi de: {nota}')