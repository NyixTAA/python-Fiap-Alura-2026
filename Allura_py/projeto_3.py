combustivel = input('Digite o tipo de combustível que deseja abastecer (E = Etanol, D = Diesel): ').upper()
qnt = float(input('Digite a quantidade de combustível que deseja abastecer (em litros): '))
preco_e = 1.7
preco_d = 2

if combustivel in ('E','ETANOL'):
    preco = preco_e * qnt
    if qnt <= 15:
        valor = preco * (preco * 0.02)
    else:
        valor = preco - (preco * 0.04)
    print(f'O valor a ser pago é de: R$e {valor:.2f}')

elif combustivel in ('D','DIESEL'):
    preco = preco_d * qnt
    if qnt <= 15:
        valor = preco - (preco * 0.03)
    else:
        valor = preco - (preco * 0.05)
    print(f'O valor a ser pago é de: R$ {valor:.2f}')
else:
    print('Digite um tipo válido!')