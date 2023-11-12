"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
while True:
    opcao = '';
    cpf_str = '';
    cpf_9_primeiros='';
    cpf_10_primeiros = '';
    resultado_1 = 0;
    soma_vezes_10_1 = 0;
    resto_1 = 0;
    verificador_1 = 0;
    i = 10;
    opcao = input('Você deseja [s]air? : ');
    if opcao.lower().startswith('s') == True:
        print('Você saiu do programa!');
        break
    cpf_str = input("Digite o seu CPF: ");
    if len(cpf_str) != 11:
        print('Você não digitou o CPF corretamente. Digite novamente');
        continue
    cpf_9_primeiros = cpf_str[:9];
    cpf_10_primeiros = cpf_str[:10];
    cpf_dois_ultimo = (cpf_str[9:]);
    print(cpf_dois_ultimo)
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
        print('CPF VÁLIDO');
        
    else:
        print('CPF INVÁLIDO');



