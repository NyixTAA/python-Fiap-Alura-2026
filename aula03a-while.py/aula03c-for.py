qtd_music = int(input('Digite a quantidade de musicas que voce tem na playlist (DB): '))

for i in range(qtd_music):
    print(f"Música {i}")

for i in range(0, 4):
    for j in range(0, 3, 2):
        print(f'i:{i}, j:{j}')