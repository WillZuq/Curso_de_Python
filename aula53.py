"""
enumerate - enumera iteráveis (índices);
"""
lista = ['Maria', 'Helena', 'Luiz'];
lista.append('João');

# lista_enumerada = enumerate(lista);
# print(next(lista_enumerada));
for item in enumerate(lista):
    print(item);
for item in enumerate(lista):
    indice, nome = item
    print(indice, nome);

lista_enumerada = list(enumerate(lista));
print(lista_enumerada);
