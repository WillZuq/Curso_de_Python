# Desempacotamento em chamadas de métodos e funções
string = 'ABCD';
lista = ['Maria', 'Helena', 'Eduarda'];
tupla = 'Python', 'é', 'legal';
# a, b, c = lista;
# print(a, c);
for nome in lista:
    print(nome, end=' ');
print(*string);
print(*tupla);

