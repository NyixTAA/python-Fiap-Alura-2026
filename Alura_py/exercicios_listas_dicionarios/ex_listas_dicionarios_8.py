produtos_doces = []
produtos_amargos = []

for id in range(1, 11):
    id = int(input(f'Digite o {id}º ID do produto: '))
    if id % 2 == 0:
        produtos_doces.append(id)
    else:
        produtos_amargos.append(id)
print(f'Produtos doces: {len(produtos_doces)}\nProdutos amargos: {len(produtos_amargos)}')