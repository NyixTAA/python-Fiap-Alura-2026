pesquisa = {
    'Design 1': 1334, 'Design 2': 982, 'Design 3': 1751,
    'Design 4': 210, 'Design 5': 1811
}
votos = 0
vencedor = ''

for design, dados in pesquisa.items():
    if dados > votos:
        votos = dados
        vencedor = design
porcentagem = (votos / sum(pesquisa.values())) * 100

print(f'Design vencedor: {vencedor}\nPorcentagem de votos recebidos: {porcentagem:.2f} %')