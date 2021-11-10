from functools import reduce

alunos = [
    {'nome' : 'Ana', 'nota' : 7.2},
    {'nome' : 'Breno', 'nota' : 8.1},
    {'nome' : 'Claudia', 'nota' : 8.7},
    {'nome' : 'Pedro', 'nota' : 6.4},
    {'nome' : 'Rafael', 'nota' : 6.7},
]


obter_nota = lambda aluno: aluno['nota']
somar = lambda a, b: a+b

# alunos_aprovados = [aluno['nota'] for aluno in alunos] pegar apena a nota do dicionário
alunos_aprovados = [aluno for aluno in alunos if aluno['nota'] >= 7] # alternativa a usar o filter
notas_dos_aprovados = [aluno['nota'] for aluno in alunos_aprovados]
total = reduce(somar, notas_dos_aprovados,0)

print (notas_dos_aprovados)
print(total / len(alunos_aprovados))
