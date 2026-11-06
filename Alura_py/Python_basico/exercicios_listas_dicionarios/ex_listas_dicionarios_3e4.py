#lista normal
lista = []
print('Digite 5 números inteiros: ')

for i in range (0, 5):
    lista.append(input())

print(lista)

#lista inversa
lista2 = []
print('\nDigite 5 números inteiros novamente: ')

for i in range (0, 5):
    lista2.append(input())

print(lista2[::-1])