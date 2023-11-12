"""
    Introdução ao try/except
    try -> tentar executar o código
    except -> Ocorreu algum erro ao tentar executar
"""
#print(1234);
#print(456);
#int('a');
numero_str = input('Vou dobrar o número que você digitar: ');
try:
    print('STR: ', numero_str);
    numero_float = float(numero_str);
    print(f'O dobro de {numero_str} é {numero_float * 2}');
except:
    print('Isso não é um número');

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_float} é {numero_float * 2}');
