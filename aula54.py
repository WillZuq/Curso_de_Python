"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua
lista. Não permita que o programa quebre
com erros de índices inexistentes na lista.
"""
import os
lista = [];
index_lista = '';
while True:
    print('Selecione uma opção: ');
    opcao = input(' [i]nserir [a]pagar [l]istar [s]air:  ');
    if opcao == 'i':
        os.system('cls');
        lista.append(input('Digite o item: '));
        continue
    elif opcao == 'a':
        os.system('cls');
        index_lista = int(input('Qual o índice do elemento que deseja deletar? '));
        try:
            del lista[index_lista];
            continue
        except:
            print('Você Digitou um índice errado. Tente novamente!');
            continue
    elif opcao == 'l':
        os.system('cls');
        for item in enumerate(lista):
            i, itens = item;
            print(i, itens);
        continue;
    elif opcao == 's':
        os.system('cls');
        print('Você saiu do programa!');
        break;
    else:
        print('Você digitou alguma coisa errada, tente novamente!');
        os.system('cls');
        continue