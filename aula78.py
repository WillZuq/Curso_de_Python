# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
l1 = [1, 2, 3, 3, 3, 3, 1];
s1 = set(l1);
l2 = list(s1)
# print(l2);

# Métodos úteis:
# add, update, clear, discard

s2 = set();
s2.add('Luiz');
s2.add(1);
s2.update(('Olá mundo', 1, 2, 3, 4));
# s2.clear();
s2.discard('Olá mundo');

# print(s2);



# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s3 = {1, 2 ,3};
s4 = {2, 3, 4};
s5 = s3 | s4;
s6 = s3 & s4;
s7 = s3 - s4;
s8 = s4 - s3;
s9 = s4 ^ s3;
print(s5);
print(s6);
print(s7);
print(s8);
print(s9);



