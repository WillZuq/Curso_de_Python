# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - Iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - ordem importa e repete valores únicos
from itertools import combinations, permutations, product
def print_iter(iterator):
    print(*list(iterator), sep = '\n');

pessoas = ['João', 'Joana', 'Luiz', 'Leticia'];
camisetas = [['preta', 'branca'], ['p', 'm', 'g'], ['masculino','feminino']];
print_iter(combinations(pessoas, 2));
print();
print_iter(permutations(pessoas, 2));
print();
print_iter(product(*camisetas))
