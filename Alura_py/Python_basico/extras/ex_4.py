inv_inicial = float(input('Digite o valor do investimento inicial: R$ '))
taxa_juros = float(input('Digite a taxa de juros mensal (em porcentagem): % ')) / 100
ap_fixo = float(input('Digite o valor do aporte fixo mensal: R$ '))
meta_total = float(input('Digite o valor da meta total desejada: R$ '))

saldo_total = inv_inicial
total_aportado = inv_inicial
juros_total = 0
mes = 0

while saldo_total < meta_total:
    mes += 1
    juros_mes = saldo_total * taxa_juros
    saldo_total += juros_mes + ap_fixo
    total_aportado += ap_fixo
    juros_total += juros_mes

    print(f'Mês {mes}:\n Juros do mês: R$ {(juros_mes):.2f}\n Saldo acumulado: R$ {(saldo_total):.2f}')

print(f'\nMeses necessários para alcançar a meta desejada: {mes}\nTotal investido: R$ {(total_aportado):.2f} \nTotal ganho com apenas juros: R$ {juros_total:.2f}')