#Programa que estebelece uma nota mínima para o estudate ter prioridade em curso de capacitação

nomeDoEstudante = input('Digite o nome: ')
nota = float(input('Digite a nota: '))
if nota >=8.0:
    print('O estudante ', nomeDoEstudante, 'tem prioridade no curso de capacitação. ')
else:
    print('O estudante', nomeDoEstudante, 'não tem prioridade no curso de capacitação. ')
