from aluno import Aluno
from disciplina import Disciplina

# criar / instanciar 1 aluno
aluno1 = Aluno("João", "123456", "Ciência da Computação")
# print(aluno1.notas_por_disciplina)

# criar / instanciar 2 disciplinas
cs = Disciplina("Computer Science", "Lucas")
dsa = Disciplina("Data Structure", "Álvaro")

#print(dsa.professor)
aluno1.matricular(cs)
aluno1.matricular(dsa)
#print(aluno1.disciplinas[0].professor, aluno1.disciplinas[0].nome)

aluno1.adicionar_nota(cs, 10)
aluno1.adicionar_nota(cs, 10)
aluno1.adicionar_nota(dsa, 8)
aluno1.adicionar_nota(dsa, 10)
print(aluno1.notas_por_disciplina)
print(aluno1.calcular_media_d(cs))
print(aluno1.calcular_media_d(dsa))