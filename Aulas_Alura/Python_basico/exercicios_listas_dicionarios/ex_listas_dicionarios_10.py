temp_med = []
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

for i in range(0, 12):
    temp = float(input(f'Digite a temperatura média de {meses[i]}: '))
    temp_med.append(temp)
media_anual = sum(temp_med) / len(temp_med)

print(f'Temperaturas acima da média: ')
for i in range(0, 12):
    if temp_med[i] > media_anual:
        print(f'{meses[i]}: {temp_med[i]} °C')
print(f'Temperatura média anual: {media_anual:.2f} °C')