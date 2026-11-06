bacterias_colonia = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
porcentagem_crescimento = []

for i in range(1, len(bacterias_colonia)):
  porcentagem = 100 * (bacterias_colonia[i] - bacterias_colonia[i-1]) / (bacterias_colonia[i-1])
  porcentagem_crescimento.append(porcentagem)
  
print(f'Porcentagens de crescimento:\n{porcentagem_crescimento}')