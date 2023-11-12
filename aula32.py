"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro
"""
# num = input('Digite um número inteiro: ');
# if num.isdigit():
#     num_int = int(num);
#     par_impar = num_int % 2 == 0;
#     par_impar_texto = 'Ímpar';
#     if par_impar:
#         par_impar_texto = 'par';
#     print(f'O número {num_int} é {par_impar_texto}');
# else:
#     print('Não é inteiro');

"""
Faça um programa que pergunte a hora ao usuário e,
baseando-se no horário descrito, exiba a saudação apropriada. Ex:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

# hora = input('Digite a hora: ');
# hora_int = int(hora[0:2:1]);
# bom_dia = hora_int <= 11 and hora_int >=0;
# boa_tarde = hora_int <= 17 and hora_int >=12;
# if bom_dia:
#     print('Bom dia');
# elif boa_tarde:
#     print('Boa Tarde');
# else:
#     print('Boa Noite');

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
nome = input('Digite seu primeiro nome: ');
n = len(nome);
if nome:
    if n <= 4:
        print ('Seu nome é curto');
    elif n >=5 and n <= 6:
        print('Seu nome é normal');
    else:
        print('Seu nome é muito grande');
else:
    print('Você não digitou um nome');

