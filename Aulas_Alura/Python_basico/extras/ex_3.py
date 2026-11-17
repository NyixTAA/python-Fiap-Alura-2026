rodando = True
total = 0
total_itens = 0
desconto = 0

print('--- CAIXA REGISTRADORA ---')
while rodando:
    preco = float(input('Preço do produto (0 para encerrar): '))
    if preco <= 0:
        break
    qnt = int(input('Quantidade: '))
    if qnt <= 0:
        print('Digite uma quantidade válida!')
        continue
    if qnt >= 10:
        subtotal = qnt * preco
        desconto += subtotal * 0.15
        total_itens += qnt
        print(f'SUBTOTAL: R$ {subtotal - desconto:.2f} (15% de desconto, preço original: R$ {subtotal})')
    else:
        subtotal = qnt * preco
        total_itens += qnt
        print(f'SUBTOTAL: R$ {subtotal:.2f}')
    total += subtotal
print(f'\n--- RESUMO DA COMPRA ---')
print(f'Total Bruto: R$ {total:.2f}')
print(f'Total Descontos: R$ {desconto:.2f}')
print(f'Total a Pagar: R$ {(total - desconto):.2f}')
print(f'Total de Itens: {total_itens}')