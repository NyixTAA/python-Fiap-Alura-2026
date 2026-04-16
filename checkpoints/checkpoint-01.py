nome = input('Digite o nome do colaborador: ')
valor_hora = float(input('Digite o valor por hora trabalhada: '))
hora_mensal = float(input('Digite a quantidade de horas trabalhadas no mês: '))
bonus = float(input('Digite o valor do bônus fixo do mês: '))
desconto = float(input('Digite o valor do desconto total do mês: '))
bruto = (valor_hora * hora_mensal) + bonus
liquido = bruto - desconto
print('-----------------------------------------------\n ---------------RESUMO FORMATADO----------------')
print(f'Colaborador:  {nome}\n Salário bruto: R${bruto}\n Salário líquido: R${liquido}')
