"""
Listas em Python
Tipos list - mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento;
Métodos úteis: 
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena lostas
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

# string = 'ABCDE' #5 caracteres (len)
# lista = [123, True, 'Luiz otávio', 1.2, []];
# print(lista);
# print(lista[2], type(lista[2]));
# lista[2] = 'Maria';
# print(lista);

# print(bool(lista));
# print(lista, type(lista));

# lista = [10, 20, 30, 40];
# # lista[2] = 300;
# # del lista[2];
# # print(lista);
# # numero = lista[2];
# lista.append(50);
# lista.pop();
# lista.append(60);
# lista.append(70);
# print(lista);

lista = [10, 20, 30, 40];
lista.append('Luiz');
nome = lista.pop();
lista.append(1234);
del lista[-1];
#lista.clear();
lista.insert(0, 5);
print(lista);

lista_a = [1, 2, 3];
lista_b = [4, 5, 6];
lista_c = lista_a + lista_b;
lista_a.extend(lista_b); #método extend mexe na variàvel que chama o método
print(lista_c);
print(lista_a);

lista_c = ['Luiz', 'Maria', 1, True];
lista_d = lista_c.copy() #mantém os valores originais da lista_c 

