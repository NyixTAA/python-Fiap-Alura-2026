dados = {
'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
}
total_idades = 0
pessoas_acima = 0

for setor, idade in dados.items():
    media_setor = sum(idade) / len(idade)
    total_idades += sum(idade)
    print(f'Média do {setor}: {media_setor}')
media_total = total_idades / (len(idade) * len(dados))

for setor, idade in dados.items():
    for id in idade:
        if id > media_total:
            pessoas_acima += 1 


print(f'Média de idade entre todos os setores: {"{:.2f}".format(media_total)}\nPessoas acima da idade média: {pessoas_acima}')