"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor
"""

def soma_lista(lista1, lista2):
    try:
        for i in lista1:
            if not isinstance(i, (int, float)):
                print('Lista 1 contém dado diferente de int e float')
        for i in lista2:
            if not isinstance(i, (int, float)):
                print('Lista 2 contém dado diferente de int e float');
        intervalo = min(len(lista1), len(lista2));
        return [
                lista1[i]+lista2[i] for i in range(intervalo)
            ]
    except TypeError:
        print('Há dado diferente de int e float')
lista1 = [1, 2, 3, 4, 5, 6, 7];
lista2 = [1, 2, 3, 4, 5];
print(soma_lista(lista1, lista2));
