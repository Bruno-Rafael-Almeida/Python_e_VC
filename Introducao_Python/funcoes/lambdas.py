from functools import reduce

alunos = [
    {'nome' : 'Ana', 'nota' : 7.2},
    {'nome' : 'Breno', 'nota' : 8.1},
    {'nome' : 'Claudia', 'nota' : 8.7},
    {'nome' : 'Pedro', 'nota' : 6.4},
    {'nome' : 'Rafael', 'nota' : 6.7},
]

aluno_aprovado = lambda aluno: aluno ['nota'] >= 7
obter_nota = lambda aluno: aluno['nota']
somar = lambda a, b: a+b

alunos_aprovados = list(filter(aluno_aprovado, alunos))
notas_dos_aprovados = list(map(obter_nota,alunos_aprovados))
total = reduce(somar, notas_dos_aprovados)
print(total / len(alunos_aprovados))

print(notas_dos_aprovados)
