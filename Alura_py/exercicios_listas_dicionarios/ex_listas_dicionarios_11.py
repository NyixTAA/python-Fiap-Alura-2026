produtos = {
'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
'Produto D': 200, 'Produto E': 250, 'Produto F': 30
}
i = 0
produto_mais_vendido = ''

print(f'Total de vendas: {sum(produtos.values())}')
for produto, valor in produtos.items():
    if valor > i:
        i = valor
        produto_mais_vendido = produto
print(f'Produto mais vendido: {produto_mais_vendido}')