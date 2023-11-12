"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
import re;
import os;
while True:
    opcao = '';
    cpf_str = '';
    cpf_9_primeiros='';
    cpf_10_primeiros = '';
    resultado_1 = 0;
    soma_vezes_10_1 = 0;
    resto_1 = 0;
    verificador_1 = 0;
    resultado_2 = 0;
    j = 11;
    i = 10;
    verificador_2 = 0;
    # cpf_str = input("Digite o seu CPF: ").replace('.', '').replace('-', '');
    cpf_str = re.sub(r'[^0-9]', '', input("Digite o seu CPF: "));
    if len(cpf_str) != 11:
        print('Você não digitou o CPF corretamente. Digite novamente');
        continue
    cpf_9_primeiros = cpf_str[:9];
    cpf_10_primeiros = cpf_str[:10];
    cpf_dois_ultimo = (cpf_str[9:]);
    for digito in cpf_9_primeiros:
        resultado_1 += int(digito) * i;
        i -= 1;
    soma_vezes_10 = resultado_1 * 10;
    resto_1 = soma_vezes_10 % 11;
    if resto_1 > 9:
        verificador_1 = 0;
    else:
        verificador_1 = resto_1;
    if verificador_1 == int(cpf_dois_ultimo[0]):
        for numero in cpf_10_primeiros:
            resultado_2 += int(numero) * j;
            j -= 1;
        soma_vezes_10_2 = resultado_2 * 10;
        resto_2 = soma_vezes_10_2 % 11;
        verificador_2 = resto_2 if resto_2 <= 9 else 0;
        if verificador_2 == int(cpf_dois_ultimo[1]):
            print('CPF VÁLIDO!');
        else:
            print('CPF INVÁLIDO!');
    else:
        print('CPF INVÁLIDO');
    opcao = input('Você deseja [s]air? : ');
    if opcao.lower().startswith('s') == True:
        print('Você saiu do programa!');
        break