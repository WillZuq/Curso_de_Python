"""
    Exercício
    Peça ao usuário para digitar o seu nome
    Peça ao usuário para digitar sua idade
    Se nome e idade forem digitados:
        Exiba:
            seu nome é {nome}
            Seu nome invertido é {nome invertido}
            Se nome contém (ou não) espaços
            Seu nome tem {n} letras
            A primeira letra do seu nome é {letra}
            A última letra do seu nome é {letra}
    Se nada for digitado em nome ou idade:
        exiba "Desculpe, você deixou campos vazios"
"""
nome = input('Digite seu nome: ');
idade = input('Digite sua idade: ');
if nome and idade:
    print(f'Seu nome é {nome}');
    n = len(nome);
    nome_invertido = nome[::-1];
    print(f'Seu nome invertido é {nome_invertido}')
    if ' ' in nome:
        print('Seu nome tem espaços');
    else:
        print('Seu nome não tem espaços')
    print(f'Seu nome tem {n} letras');
    print(f'A primeira letra do seu nome é {nome[0]}');
    print(f'A última letra do seu nome é {nome[n-1]}');
else:
    print('Desculpa, você deixou campos vazios');

