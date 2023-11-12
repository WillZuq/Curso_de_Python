"""
args - Argumentos não nomeados
* - *args(empacotamento e desempacotamento)
"""
#Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0;
    # print(args, type(args));
    for numero in args:
        # print('Total', total, numero)
        total += numero
    return total;


soma_total = soma(1, 2, 3, 4, 5, 6)
print(soma_total);
# print(sum(1, 2, 3, 4, 5, 6));
