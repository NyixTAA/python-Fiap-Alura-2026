salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]

dic_abono = {}
total_gastos = 0
colaboradores_abono_min = 0
maior_abono = 0
for i in salarios:
    abono = i * 0.1
    if abono < 200:
        abono = 200
        colaboradores_abono_min += 1
    if abono > maior_abono:
        maior_abono = abono
    total_gastos += abono
    dic_abono[i] = (f'R$ {abono:.2f}')
print(f'Dicionário de abonos: {dic_abono}\nTotal gasto com abono: R$ {total_gastos:.2f}\nColaboradores com abono mínimo: {colaboradores_abono_min}\nMaior abono: R$ {maior_abono:.2f}')