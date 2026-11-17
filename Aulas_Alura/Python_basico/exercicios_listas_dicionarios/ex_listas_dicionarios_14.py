diversidade = {
'Área Norte': [2819, 7236],
'Área Leste': [1440, 9492],
'Área Sul': [5969, 7496],
'Área Oeste': [14446, 49688],
'Área Centro': [22558, 45148]
 }
maior_media_bio = 0
maior_media_area = ''

for area, especie in diversidade.items():
    especie = sum(especie) / len(especie)
    print(f'Média da {area}: {especie}')
    if especie > maior_media_bio:
        maior_media_bio = especie
        maior_media_area = area
print(f'\nÁrea com maior diversidade biológica: {maior_media_area}')