lista = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
compras_3000 = 0
compras = len(lista)

print(f'A média da lista é: {sum(lista) / len(lista)}')

for elemento in lista:
    if elemento >= 3000:
        compras_3000 += 1
print(f'Compras acima de R$ 3000: {compras_3000}\nPorcentagem de compras acima de R$ 3000: {(compras_3000 / len(lista)) * 100}%')