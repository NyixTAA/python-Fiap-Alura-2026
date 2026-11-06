qnt_vendas1 = int(input('Digite a quantidade de vendas durante 2022: '))
qnt_vendas2 = int(input('Digite a quantidade de vendas durante 2023: '))

variacao = ((qnt_vendas2 - qnt_vendas1) / qnt_vendas1) * 100

if variacao >= 20:
    bonificacao = 'haverá uma bonificação para o time de vendas!'
elif variacao >= 2:
    bonificacao = 'haverá uma pequena bonificação para o time de vendas!'
elif variacao >= -10:
    bonificacao = 'deve haver um planejamento de políticas de incentivo às vendas.'
else:
    bonificacao = 'deve haver um corte de gastos.'
print(f'A variação percentual de vendas é de: {variacao}, isso significa que {bonificacao}')