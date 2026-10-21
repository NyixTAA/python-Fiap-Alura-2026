numero = int(input('Digite um número: '))
print(f'\nNúmeros primos de 1 a {numero}:')
lista = []

for i in range(2, numero):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lista.append(i)
print(lista)