# Nota-Mínima-para-Prioridade-em-Curso
#Programa, em Python, que estabelece um nota mínima para que um estudante possa ter prioridade em curso de capacitação.

nomeDoEstudante = input('Digite o nome: ')
nota = float(input('Digite a nota: '))
if nota >=8.0:
    print('O estudante ', nomeDoEstudante, 'tem prioridade no curso de capacitação. ')
else:
    print('O estudante', nomeDoEstudante, 'não tem prioridade no curso de capacitação. ')

