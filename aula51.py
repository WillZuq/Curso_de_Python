"""
Introdução ao desempacotamento
"""
nomes = ['Maria', 'Helena', 'Luiz'];
# nome1, nome2, nome3 = nomes;
nome1, *_ = nomes;
print(nome1);
