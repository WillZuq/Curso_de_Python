"""
Argumentos nomeados e não nomeados em funções PYthon
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento(valor)
"""
def soma(x, y):
    print(f'x = {x} y = {y} | x + y = {x+y}');
soma(1, 2);
soma(y=2, x=1);