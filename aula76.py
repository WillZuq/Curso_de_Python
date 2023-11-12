import copy
# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')
# pessoa = {
#     'nome': 'Luiz otávio',
#     'sobrenome' : 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal rua', 'número': 123},
#         {'rua': 'outra rua','número': 321}
#     ]
# }

# # print(pessoa, type(pessoa));
# print(pessoa['nome']);
# print();
# for chave in pessoa:
#     print(chave, pessoa[chave]);

#Manipulando chaves e valores em dicionários

# pessoa = {};
# chave = 'nome';
# pessoa[chave] = 'Luiz Otávio';
# pessoa['sobrenome'] = 'Miranda';
# pessoa[chave] = 'Maria';
# del pessoa['sobrenome'];
# print(pessoa);
# print(pessoa[chave]);
# # print(pessoa['sobrenome']);
# print(pessoa.get('Sobrenome'));

#Métodos úteis dos dicionários em Python
#len - quantas chaves
#Keys - iteráveis com as chaves
#values - iterável com os valores
#items - iterável com chaves e valores
#setdefault - adiciona valor se a chave não existe
#copy - retorna uma cópia rasa (shallow copy)
#pop - apaga um item com a chave especificada (del)
#popitem - apaga o último item adicionado
#update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Luiz otávio',
    'sobrenome' : 'Miranda',
    'idade': 18,
    'altura': 1.8,
}
pessoa.setdefault('Endereco', None);
print(len(pessoa));
print(list(pessoa.keys()));
print(list(pessoa.values()));
print(list(pessoa.items()));
print();
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
# d2 = d1 ERRADO!
# d2 = d1.copy(); # Shallow copy
d2 = copy.deepcopy(d1);
d2['c1'] = 1000;
d2['l1'][1] = 99999;
print(d1);
print(d2);
print();
p1 = {
    'nome' : 'Luiz',
    'sobrenome': 'Miranda',
}
# print(p1.get('nome'));
# print(p1.get('nome', 'Não existe'));
# nome = p1.pop('nome');
# ultima_chave = p1.popitem();
# print(ultima_chave);
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# });
# p1.update(nome = 'novo valor', idade = 30);
tupla = (('nome', 'novo valor'),('idade', 30))
p1.update(tupla)
print(p1);