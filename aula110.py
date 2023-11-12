# groupby - agrupando valores (itertools)
from itertools import groupby
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letíca', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'JOana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]
# alunos = ['a', 'a', 'a', 'b', 'c'];
# grupos = groupby(alunos)
# for chave, grupo in grupos:
#     print(list(grupo));
alunos_agrupados = sorted(alunos, key = lambda a: a['nota'])
grupos = groupby(alunos_agrupados, key = lambda a: a['nota']);
for chave, grupo in grupos:
    print(chave);
    for aluno in grupo:
        print(aluno);