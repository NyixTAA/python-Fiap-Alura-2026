col_A = 4
col_B = 10

taxa_cresc1 = 0.03
taxa_cresc2 = 0.015

dias = 0

while col_A <= col_B:
    col_A *= 1 + taxa_cresc1
    col_B *= 1 + taxa_cresc2
    dias += 1

print(f'Irá levar {dias} dias para a colônia A ultrapassar a colônia B')